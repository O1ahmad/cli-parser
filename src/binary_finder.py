#!/usr/bin/env python3
"""
Binary Finder Module - Locate binaries in Docker containers and host systems

Features:
- Efficient single-pass filesystem search using find command
- Substring matching for tool name discovery
- Caching to avoid repeated scans
- 2-minute timeout for large container images
"""
import os
import re
import subprocess
from typing import Optional, List, Tuple, Set
from pathlib import Path


class BinaryFinder:
    """Find binaries in Docker containers and host systems"""

    # Cache for container scans to avoid repeated searches
    _container_cache = {}

    # Timeout for container operations (2 minutes)
    CONTAINER_TIMEOUT = 120

    @staticmethod
    def find_on_host(binary_name: str) -> Tuple[Optional[str], str]:
        """
        Find binary on host system

        Args:
            binary_name: Name of binary to find

        Returns:
            Tuple of (binary_path, discovery_method) or (None, "not_found")
        """
        # Try which command first (fastest)
        try:
            result = subprocess.run(
                ['which', binary_name],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip(), "which"
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass

        # Try common locations
        common_paths = [
            '/usr/bin',
            '/usr/local/bin',
            '/bin',
            '/opt/bin',
            os.path.expanduser('~/.local/bin')
        ]

        for path in common_paths:
            binary_path = Path(path) / binary_name
            if binary_path.exists() and os.access(binary_path, os.X_OK):
                return str(binary_path), "common_path"

        return None, "not_found"

    @staticmethod
    def find_in_container(docker_image: str, binary_name: str) -> Tuple[Optional[str], str]:
        """
        Find binary in Docker container

        Args:
            docker_image: Full Docker image name (e.g., "alpine:latest")
            binary_name: Name of binary to find

        Returns:
            Tuple of (binary_path, discovery_method) or (None, "not_found")
        """
        # Try which command in container first (fastest)
        try:
            result = subprocess.run(
                ['docker', 'run', '--rm', '--entrypoint', 'which', docker_image, binary_name],
                capture_output=True,
                text=True,
                timeout=30
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip(), "which_in_container"
        except subprocess.TimeoutExpired:
            pass

        # Try command -v (works in more minimal containers)
        try:
            result = subprocess.run(
                ['docker', 'run', '--rm', '--entrypoint', 'sh', docker_image,
                 '-c', f'command -v {binary_name}'],
                capture_output=True,
                text=True,
                timeout=30
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip(), "command_v"
        except subprocess.TimeoutExpired:
            pass

        return None, "not_found"

    @staticmethod
    def discover_all_executables(docker_image: str, use_cache: bool = True) -> List[str]:
        """
        Discover all executable files in a Docker container using efficient find command

        Args:
            docker_image: Full Docker image name
            use_cache: Whether to use cached results

        Returns:
            List of executable file paths found in container
        """
        # Check cache first
        if use_cache and docker_image in BinaryFinder._container_cache:
            return BinaryFinder._container_cache[docker_image]

        print(f"  → Scanning container filesystem for executables (timeout: {BinaryFinder.CONTAINER_TIMEOUT}s)...")

        # Efficient find command from root, excluding pseudo-filesystems
        find_cmd = [
            'docker', 'run', '--rm', '--entrypoint', 'sh', docker_image,
            '-c',
            'find / -type f -executable '
            '-not -path "/proc/*" '
            '-not -path "/sys/*" '
            '-not -path "/dev/*" '
            '-not -path "/var/*" '
            '-not -path "*/.git/*" '
            '2>/dev/null || true'
        ]

        try:
            result = subprocess.run(
                find_cmd,
                capture_output=True,
                text=True,
                timeout=BinaryFinder.CONTAINER_TIMEOUT
            )

            if result.returncode in [0, 1]:  # 0 = success, 1 = some files not found (OK)
                executables = [line.strip() for line in result.stdout.split('\n') if line.strip()]
                print(f"  → Found {len(executables)} executables")

                # Cache results
                BinaryFinder._container_cache[docker_image] = executables
                return executables
            else:
                print(f"  → Find command failed with exit code {result.returncode}")
                return []

        except subprocess.TimeoutExpired:
            print(f"  → Timeout after {BinaryFinder.CONTAINER_TIMEOUT}s (large image or slow filesystem)")
            return []
        except Exception as e:
            print(f"  → Error scanning container: {e}")
            return []

    @staticmethod
    def generate_candidates(tool_name: str, min_length: int = 2) -> Set[str]:
        """
        Generate candidate binary names by simply splitting tool name into words

        Args:
            tool_name: Tool name from config (e.g., "Apache Drill" or "kubectl")
            min_length: Minimum word length to consider (default 2 for short tools like "go", "jq")

        Returns:
            Set of words to search for in binary names
        """
        # Normalize and split into words
        normalized = tool_name.lower()
        words = re.split(r'[\s\-_]+', normalized)

        # Remove common prefix words that aren't part of binary names
        ignore_words = {'the', 'a', 'an', 'apache', 'project', 'foundation'}
        words = [w for w in words if w and w not in ignore_words and len(w) >= min_length]

        return set(words)

    @staticmethod
    def verify_executable_responds_to_help(binary_path: str, docker_image: str) -> bool:
        """
        Quick check if binary responds to basic help commands

        Args:
            binary_path: Path to binary
            docker_image: Docker image to test in

        Returns:
            True if binary responds to --help, -h, or help
        """
        import subprocess

        # Try quick help variations (2 second timeout each)
        help_variations = ['--help', '-h', 'help']

        for help_arg in help_variations:
            try:
                # Use --entrypoint to explicitly specify the binary we want to test
                result = subprocess.run(
                    ['docker', 'run', '--rm', '--entrypoint', binary_path, docker_image, help_arg],
                    capture_output=True,
                    text=True,
                    timeout=2
                )

                output = (result.stdout + result.stderr).strip()

                # Check if we got any meaningful output
                if len(output) > 50 and result.returncode in [0, 1]:
                    return True

            except (subprocess.TimeoutExpired, Exception):
                continue

        return False

    @staticmethod
    def match_executables_to_candidates(
        executables: List[str],
        candidates: Set[str],
        docker_image: Optional[str] = None,
        verify_help: bool = False
    ) -> List[Tuple[str, str, float]]:
        """
        Match executables that contain any of the candidate words

        Args:
            executables: List of full paths to executables
            candidates: Set of words to search for
            docker_image: Optional Docker image for verification
            verify_help: If True, verify executable responds to help commands

        Returns:
            List of (exe_path, match_type, confidence) tuples, sorted by match quality
        """
        matches = []

        # Skip common system binaries and script files
        skip_binaries = {'sh', 'bash', 'ls', 'cat', 'echo', 'true', 'false', 'test', 'id', 'tr', 'ar', 'as'}
        skip_extensions = {'.js', '.ts', '.d.ts', '.json', '.py', '.rb', '.pl', '.sh', '.txt', '.md', '.xml', '.html'}

        for exe_path in executables:
            exe_name = os.path.basename(exe_path)
            exe_name_lower = exe_name.lower()

            # Skip system binaries and scripts
            if exe_name in skip_binaries:
                continue
            if any(exe_name.endswith(ext) for ext in skip_extensions):
                continue

            # Check if any candidate word is in the executable name (case-insensitive)
            for word in candidates:
                if word in exe_name_lower:
                    # Simple confidence based on match quality
                    if exe_name_lower == word:
                        confidence = 1.0
                        match_type = 'exact'
                    elif exe_name_lower.startswith(word):
                        confidence = 0.9
                        match_type = 'starts_with'
                    else:
                        confidence = 0.7
                        match_type = 'contains'

                    # Bonus for binaries in standard locations
                    if '/usr/bin/' in exe_path or '/usr/local/bin/' in exe_path:
                        confidence = min(confidence + 0.1, 1.0)

                    # Optional: Verify it responds to help (quick check)
                    if verify_help and docker_image:
                        if not BinaryFinder.verify_executable_responds_to_help(exe_path, docker_image):
                            # Penalize if it doesn't respond to help
                            confidence *= 0.5

                    matches.append((exe_path, match_type, confidence))
                    break  # Only count each executable once

        # Sort by confidence (highest first), then by path length (shorter preferred)
        matches.sort(key=lambda x: (-x[2], len(x[0])))

        return matches

    @staticmethod
    def discover_binaries_for_tool(docker_image: str, tool_name: str) -> List[Tuple[str, str, float]]:
        """
        Main discovery method - find all matching binaries for a tool

        Args:
            docker_image: Docker image to search in
            tool_name: Name of the tool

        Returns:
            List of (binary_path, match_type, confidence) tuples
        """
        print(f"\n  Discovering binaries for: {tool_name}")
        print(f"  Image: {docker_image}")

        # Generate candidates
        candidates = BinaryFinder.generate_candidates(tool_name)
        print(f"  → Generated {len(candidates)} candidates: {', '.join(sorted(candidates)[:10])}{'...' if len(candidates) > 10 else ''}")

        # Try quick direct lookup first
        for candidate in sorted(candidates, key=len, reverse=True)[:5]:  # Try top 5 most likely
            binary_path, method = BinaryFinder.find_in_container(docker_image, candidate)
            if binary_path:
                print(f"  → Quick match found: {binary_path} (method: {method})")
                return [(binary_path, method, 1.0)]

        # Fall back to full filesystem scan
        print(f"  → Quick lookup failed, performing full scan...")
        executables = BinaryFinder.discover_all_executables(docker_image)

        if not executables:
            print(f"  → No executables found in container")
            return []

        # Match executables to candidates (with help verification)
        matches = BinaryFinder.match_executables_to_candidates(
            executables,
            candidates,
            docker_image=docker_image,
            verify_help=True  # Enable help verification
        )

        if matches:
            print(f"  → Found {len(matches)} matches")
            # Show top 5 matches
            for exe_path, match_type, confidence in matches[:5]:
                print(f"     • {os.path.basename(exe_path)} ({match_type}, confidence: {confidence:.2f})")
        else:
            print(f"  → No matches found")

        return matches
