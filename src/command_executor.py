#!/usr/bin/env python3
"""
Command Executor Module - Execute commands in Docker containers with fallback strategies

Features:
- Multiple help command variations (--help, -h, help, etc.)
- Version detection with fallbacks
- 2-minute timeout for slow commands
- Error handling and validation
"""
import subprocess
from typing import Optional, Dict, List, Tuple


class CommandExecutor:
    """Execute commands in Docker containers and on host"""
    
    # Timeout for command execution (2 minutes)
    COMMAND_TIMEOUT = 120
    
    # Help command variations to try (in order of preference)
    HELP_VARIATIONS = [
        ['--help'],
        ['-h'],
        ['help'],
        ['-help'],
        ['--usage'],
        [],  # No args - some tools print help by default
    ]
    
    # Version command variations to try
    VERSION_VARIATIONS = [
        ['--version'],
        ['-v'],
        ['version'],
        ['-version'],
        ['--v'],
    ]
    
    @staticmethod
    def execute_command(
        binary_path: str,
        args: List[str],
        docker_image: Optional[str] = None,
        timeout: int = None
    ) -> Tuple[int, str, str]:
        """
        Execute a command and return result
        
        Args:
            binary_path: Path to binary
            args: Command arguments
            docker_image: Optional Docker image to run in
            timeout: Timeout in seconds (default: COMMAND_TIMEOUT)
            
        Returns:
            Tuple of (exit_code, stdout, stderr)
        """
        if timeout is None:
            timeout = CommandExecutor.COMMAND_TIMEOUT
        
        if docker_image:
            # Run in Docker container
            # For containers, we need to check if the binary is the entrypoint
            # If it is, don't repeat it; if not, pass it explicitly
            import os
            binary_name = os.path.basename(binary_path)
            
            # Try without specifying binary (assumes it's in entrypoint)
            cmd = ['docker', 'run', '--rm', docker_image] + args
        else:
            # Run on host
            cmd = [binary_path] + args
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            return result.returncode, result.stdout, result.stderr
            
        except subprocess.TimeoutExpired:
            return -1, '', f'Timeout after {timeout}s'
        except FileNotFoundError:
            return -1, '', f'Binary not found: {binary_path}'
        except Exception as e:
            return -1, '', str(e)
    
    @staticmethod
    def is_valid_help_output(output: str, exit_code: int) -> bool:
        """
        Check if output looks like valid help text
        
        Args:
            output: Command output (stdout + stderr)
            exit_code: Exit code from command
            
        Returns:
            True if output appears to be valid help text
        """
        # Exit code check - help commands typically return 0 or 1
        if exit_code not in [0, 1, 2]:
            return False
        
        # Must have reasonable amount of content
        if len(output) < 50:
            return False
        
        # Check for help indicators (case-insensitive)
        output_lower = output.lower()
        help_indicators = [
            'usage:', 'usage :', 'usage:',
            'options:', 'flags:',
            'commands:', 'subcommands:',
            'help', 'examples:',
            'arguments:',
            'synopsis',
            'description:',
        ]
        
        has_indicator = any(indicator in output_lower for indicator in help_indicators)
        
        # Or has option-like patterns (--something or -x)
        has_options = ('--' in output or ' -' in output)
        
        return has_indicator or has_options
    
    @staticmethod
    def execute_help(
        binary_path: str,
        parent_command: Optional[str] = None,
        docker_image: Optional[str] = None
    ) -> Optional[str]:
        """
        Execute help command with fallback strategies
        
        Args:
            binary_path: Path to binary
            parent_command: Optional parent command (e.g., "config" for "git config")
            docker_image: Optional Docker image to run in
            
        Returns:
            Help text or None if all attempts fail
        """
        # Build command parts
        if parent_command:
            # For subcommands like "git config --help"
            cmd_parts = parent_command.split()
        else:
            cmd_parts = []
        
        # Try each help variation
        for help_args in CommandExecutor.HELP_VARIATIONS:
            full_args = cmd_parts + help_args
            
            exit_code, stdout, stderr = CommandExecutor.execute_command(
                binary_path,
                full_args,
                docker_image,
                timeout=10  # Shorter timeout for help commands (reduced from 30s)
            )
            
            # Combine stdout and stderr (some tools print help to stderr)
            output = stdout + '\n' + stderr
            output = output.strip()
            
            if CommandExecutor.is_valid_help_output(output, exit_code):
                return output
        
        return None
    
    @staticmethod
    def execute_version(
        binary_path: str,
        docker_image: Optional[str] = None
    ) -> Optional[str]:
        """
        Execute version command with fallback strategies
        
        Args:
            binary_path: Path to binary
            docker_image: Optional Docker image to run in
            
        Returns:
            Version text or None if all attempts fail
        """
        # Try each version variation
        for version_args in CommandExecutor.VERSION_VARIATIONS:
            exit_code, stdout, stderr = CommandExecutor.execute_command(
                binary_path,
                version_args,
                docker_image,
                timeout=10  # Shorter timeout for version commands (reduced from 30s)
            )
            
            # Combine stdout and stderr
            output = stdout + '\n' + stderr
            output = output.strip()
            
            # Version output typically has version numbers
            if output and (exit_code in [0, 1]) and len(output) > 0:
                # Check if it looks like version output (has numbers)
                import re
                if re.search(r'\d+\.\d+', output):
                    return output
        
        return None
    
    @staticmethod
    def test_help_variations(
        binary_path: str,
        docker_image: Optional[str] = None
    ) -> Dict[str, any]:
        """
        Test all help command variations and return detailed results
        
        Args:
            binary_path: Path to binary
            docker_image: Optional Docker image to run in
            
        Returns:
            Dict with test results for each variation
        """
        results = {
            'binary': binary_path,
            'image': docker_image,
            'tests': [],
            'working_commands': [],
            'best_command': None
        }
        
        for help_args in CommandExecutor.HELP_VARIATIONS:
            exit_code, stdout, stderr = CommandExecutor.execute_command(
                binary_path,
                help_args,
                docker_image,
                timeout=30
            )
            
            output = stdout + '\n' + stderr
            output = output.strip()
            
            is_valid = CommandExecutor.is_valid_help_output(output, exit_code)
            
            cmd_str = ' '.join(help_args) if help_args else '(no args)'
            
            test_result = {
                'command': cmd_str,
                'args': help_args,
                'exit_code': exit_code,
                'output_length': len(output),
                'is_valid': is_valid
            }
            
            results['tests'].append(test_result)
            
            if is_valid:
                results['working_commands'].append(cmd_str)
                if not results['best_command']:
                    results['best_command'] = cmd_str
        
        return results
    
    @staticmethod
    def verify_binary(
        binary_path: str,
        docker_image: Optional[str] = None
    ) -> bool:
        """
        Verify that a binary exists and can be executed
        
        Args:
            binary_path: Path to binary
            docker_image: Optional Docker image to run in
            
        Returns:
            True if binary can be executed
        """
        # Try to get help text
        help_text = CommandExecutor.execute_help(binary_path, docker_image=docker_image)
        return help_text is not None and len(help_text) > 50


