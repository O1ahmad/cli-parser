#!/usr/bin/env python3
"""
CLI Tools Processor V2 - Batch process multiple CLI tools with parallel execution support

Features:
- Reliable binary finding in containers
- Parallel processing for faster throughput
- Subset filtering (--only flag)
- Progress tracking and detailed logging
- Resume support (skip already processed)
"""
import argparse
import json
import os
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# Add src to path
sys.path.insert(0, os.path.dirname(__file__))

import parser

from binary_finder import BinaryFinder


class ToolsProcessor:
    """Process multiple CLI tools from configuration"""

    def __init__(self, config_file: str, output_dir: str, max_depth: int = 20, skip_existing: bool = True):
        self.config_file = Path(config_file)
        self.output_dir = Path(output_dir)
        self.max_depth = max_depth
        self.skip_existing = skip_existing

        self.stats = {"total": 0, "success": 0, "failed": 0, "skipped": 0, "start_time": datetime.now()}

    def log(self, message: str, level: str = "INFO"):
        """Log message with timestamp"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {level}: {message}")

    def load_config(self) -> Dict:
        """Load tools configuration from JSON file"""
        with open(self.config_file, "r") as f:
            config = json.load(f)

        # Determine category key
        if "dev_tools" in config:
            category_key = "dev_tools"
        elif "blockchain_tools" in config:
            category_key = "blockchain_tools"
        elif "cncf_tools" in config:
            category_key = "cncf_tools"
        else:
            # Find first array key
            for key in config.keys():
                if isinstance(config[key], list):
                    category_key = key
                    break
            else:
                raise ValueError("No tools array found in config")

        return config, category_key

    def filter_tools(self, tools: List[Dict], only_tools: Optional[List[str]] = None) -> List[Dict]:
        """Filter tools based on criteria"""
        filtered = []

        for tool in tools:
            name = tool.get("name", "Unknown")

            # Skip if only_tools specified and not in list
            if only_tools and name not in only_tools:
                continue

            # Skip deprecated
            if tool.get("deprecated", False):
                self.log(f"Skipping {name}: deprecated")
                continue

            # Must have required fields
            if not tool.get("image_name") or not tool.get("docker_help_command"):
                self.log(f"Skipping {name}: missing required fields")
                continue

            filtered.append(tool)

        return filtered

    def get_output_path(self, tool_name: str, category: str, image_tag: str) -> Path:
        """Get output file path for a tool"""
        safe_name = tool_name.replace(" ", "_").replace("/", "_").lower()
        filename = f"{safe_name}-{image_tag}.json"

        category_dir = self.output_dir / category
        category_dir.mkdir(parents=True, exist_ok=True)

        return category_dir / filename

    def process_tool(self, tool: Dict, category: str) -> Dict:
        """
        Process a single tool

        Returns:
            Result dict with status and details
        """
        name = tool["name"]
        image_name = tool["image_name"]
        docker_help_command = tool["docker_help_command"]

        # Handle both image_tag (string) and image_tags (array)
        if "image_tag" in tool:
            docker_tag = tool["image_tag"]
        else:
            # Handle empty list with `or` fallback to prevent IndexError
            image_tags = tool.get("image_tags", ["latest"]) or ["latest"]
            docker_tag = "latest" if "latest" in image_tags else image_tags[0]

        docker_image = f"{image_name}:{docker_tag}"

        # Extract binary name from help command
        binary_name = docker_help_command.split()[0]

        # Get output path
        output_path = self.get_output_path(name, category, docker_tag)

        # Check if already exists
        if self.skip_existing and output_path.exists():
            return {"name": name, "status": "skipped", "message": "already exists", "output_path": str(output_path)}

        try:
            # Parse the tool
            result = parser.parse_binary(binary_name, docker_image=docker_image, max_depth=self.max_depth)

            if not result:
                return {"name": name, "status": "failed", "message": "parsing returned no results"}

            # Validate result has meaningful data
            num_commands = len(result.get("subcommands", []))
            num_options = len(result.get("options", []))

            if num_commands == 0 and num_options < 3:
                return {
                    "name": name,
                    "status": "failed",
                    "message": f"insufficient data: {num_commands} commands, {num_options} options",
                }

            # Save result
            with open(output_path, "w") as f:
                json.dump(result, f, indent=2)

            file_size = output_path.stat().st_size / 1024  # KB

            return {
                "name": name,
                "status": "success",
                "output_path": str(output_path),
                "size_kb": file_size,
                "commands": num_commands,
                "options": num_options,
                "version": result.get("version"),
            }

        except Exception as e:
            return {"name": name, "status": "failed", "message": str(e)[:200]}

    def process_tools_sequential(self, tools: List[Dict], category: str) -> List[Dict]:
        """Process tools sequentially (for debugging or when parallelization issues occur)"""
        results = []

        for i, tool in enumerate(tools, 1):
            self.log(f"[{i}/{len(tools)}] Processing: {tool['name']}")

            result = self.process_tool(tool, category)
            results.append(result)

            # Update stats
            self.stats["total"] += 1
            if result["status"] == "success":
                self.stats["success"] += 1
                self.log(
                    f"  ✓ Success: {result.get('size_kb', 0):.1f} KB, "
                    f"{result.get('commands', 0)} cmds, {result.get('options', 0)} opts"
                )
            elif result["status"] == "skipped":
                self.stats["skipped"] += 1
                self.log(f"  ⊙ Skipped: {result.get('message', '')}")
            else:
                self.stats["failed"] += 1
                self.log(f"  ✗ Failed: {result.get('message', '')}", "ERROR")

        return results

    def process_tools_parallel(self, tools: List[Dict], category: str, max_workers: int = 4) -> List[Dict]:
        """Process tools in parallel for faster throughput"""
        results = []

        with ProcessPoolExecutor(max_workers=max_workers) as executor:
            # Submit all jobs
            future_to_tool = {executor.submit(self.process_tool, tool, category): tool for tool in tools}

            # Process completed jobs
            for future in as_completed(future_to_tool):
                tool = future_to_tool[future]

                try:
                    result = future.result()
                    results.append(result)

                    # Update stats
                    self.stats["total"] += 1
                    if result["status"] == "success":
                        self.stats["success"] += 1
                        self.log(
                            f"✓ {result['name']}: {result.get('size_kb', 0):.1f} KB, "
                            f"{result.get('commands', 0)} cmds"
                        )
                    elif result["status"] == "skipped":
                        self.stats["skipped"] += 1
                        self.log(f"⊙ {result['name']}: skipped")
                    else:
                        self.stats["failed"] += 1
                        self.log(f"✗ {result['name']}: {result.get('message', '')}", "ERROR")

                except Exception as e:
                    self.stats["total"] += 1
                    self.stats["failed"] += 1
                    self.log(f"✗ {tool['name']}: {str(e)[:100]}", "ERROR")
                    results.append({"name": tool["name"], "status": "failed", "message": str(e)[:200]})

        return results

    def process(self, only_tools: Optional[List[str]] = None, parallel: bool = False, max_workers: int = 4):
        """
        Main processing method

        Args:
            only_tools: If set, only process these tools
            parallel: Whether to process in parallel
            max_workers: Number of parallel workers
        """
        self.log("=" * 80)
        self.log(f"CLI Tools Processor V2")
        self.log("=" * 80)
        self.log(f"Config: {self.config_file}")
        self.log(f"Output: {self.output_dir}")
        self.log(f"Max Depth: {self.max_depth}")
        self.log(f"Parallel: {parallel} (workers: {max_workers if parallel else 'N/A'})")
        self.log("=" * 80)

        # Load config
        config, category_key = self.load_config()
        tools = config[category_key]

        self.log(f"Loaded {len(tools)} tools from '{category_key}' category")

        # Filter tools
        filtered_tools = self.filter_tools(tools, only_tools)

        if not filtered_tools:
            self.log("No tools to process after filtering", "WARN")
            return

        self.log(f"Processing {len(filtered_tools)} tools")
        self.log("=" * 80)

        # Process tools
        if parallel:
            results = self.process_tools_parallel(filtered_tools, category_key, max_workers)
        else:
            results = self.process_tools_sequential(filtered_tools, category_key)

        # Print summary
        self.print_summary(results)

    def print_summary(self, results: List[Dict]):
        """Print processing summary"""
        duration = (datetime.now() - self.stats["start_time"]).total_seconds()

        self.log("=" * 80)
        self.log("PROCESSING SUMMARY")
        self.log("=" * 80)
        self.log(f"Duration: {duration:.1f}s")
        self.log(f"Total: {self.stats['total']}")
        self.log(f"✓ Success: {self.stats['success']}")
        self.log(f"⊙ Skipped: {self.stats['skipped']}")
        self.log(f"✗ Failed: {self.stats['failed']}")

        # Show successful results
        successful = [r for r in results if r["status"] == "success"]
        if successful:
            self.log("=" * 80)
            self.log(f"SUCCESSFUL EXTRACTIONS ({len(successful)})")
            self.log("=" * 80)
            for r in successful:
                self.log(
                    f"  • {r['name']}: {r.get('size_kb', 0):.1f} KB, "
                    f"{r.get('commands', 0)} cmds, {r.get('options', 0)} opts"
                )

        # Show failures
        failed = [r for r in results if r["status"] == "failed"]
        if failed:
            self.log("=" * 80)
            self.log(f"FAILED ({len(failed)})")
            self.log("=" * 80)
            for r in failed:
                self.log(f"  • {r['name']}: {r.get('message', 'unknown error')}")

        success_rate = (self.stats["success"] / self.stats["total"] * 100) if self.stats["total"] > 0 else 0
        self.log("=" * 80)
        self.log(f"Success Rate: {success_rate:.1f}%")
        self.log("=" * 80)


def main():
    """CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Process multiple CLI tools from configuration",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument("config", help="Path to config JSON file")
    parser.add_argument("--output-dir", default="data/results", help="Base output directory")
    parser.add_argument("--max-depth", type=int, default=20, help="Maximum recursion depth (default: 20)")
    parser.add_argument("--only", nargs="+", help="Only process these tools (by name)")
    parser.add_argument("--parallel", action="store_true", help="Process tools in parallel")
    parser.add_argument("--workers", type=int, default=4, help="Number of parallel workers (default: 4)")
    parser.add_argument("--no-skip", action="store_true", help="Reprocess even if output exists")

    args = parser.parse_args()

    # Create processor
    processor = ToolsProcessor(args.config, args.output_dir, max_depth=args.max_depth, skip_existing=not args.no_skip)

    # Process tools
    processor.process(only_tools=args.only, parallel=args.parallel, max_workers=args.workers)


if __name__ == "__main__":
    main()
