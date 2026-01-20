#!/usr/bin/env python3
"""
Binary Discovery Tool - Discover and validate binaries for CLI tools in Docker images

This tool processes CLI tools that don't have binary names defined and attempts to:
1. Discover executables in their Docker images using efficient find from root (/)
2. Match executables to tool names using substring matching
3. Test help commands to verify binaries work
4. Update configuration with discovered binaries

Features:
- Efficient single-pass filesystem search with 2-minute timeout
- Substring matching for fuzzy binary name discovery
- Validation that help commands work
- Dry-run mode for testing
- Detailed progress reporting
"""
import argparse
import json
import sys
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
import subprocess

# Add src to path
sys.path.insert(0, os.path.dirname(__file__))

from binary_finder import BinaryFinder
from command_executor import CommandExecutor


class BinaryDiscoveryTool:
    """Discover binaries for tools without binary names"""
    
    def __init__(self, config_file: str, dry_run: bool = False):
        """
        Initialize the discovery tool
        
        Args:
            config_file: Path to cli_tools.json config file
            dry_run: If True, don't update config file
        """
        self.config_file = Path(config_file)
        self.dry_run = dry_run
        self.config = None
        self.tools = []
        
        self.stats = {
            'total': 0,
            'success': 0,
            'partial': 0,  # Found binary but help doesn't work
            'failed': 0,
            'skipped': 0,
            'start_time': datetime.now()
        }
    
    def log(self, message: str, level: str = "INFO"):
        """Log message with timestamp"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] {level}: {message}")
    
    def load_config(self) -> bool:
        """Load configuration file"""
        try:
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
            
            self.tools = self.config.get('cli_tools', [])
            self.log(f"Loaded {len(self.tools)} tools from config")
            return True
            
        except Exception as e:
            self.log(f"Failed to load config: {e}", "ERROR")
            return False
    
    def save_config(self):
        """Save updated configuration file"""
        if self.dry_run:
            self.log("Dry-run mode: skipping config save", "INFO")
            return
        
        try:
            # Create backup
            backup_path = self.config_file.with_suffix('.json.backup')
            with open(backup_path, 'w') as f:
                json.dump(self.config, f, indent=2)
            self.log(f"Created backup: {backup_path}")
            
            # Save updated config
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            self.log(f"Updated config saved: {self.config_file}")
            
        except Exception as e:
            self.log(f"Failed to save config: {e}", "ERROR")
    
    def check_docker_available(self) -> bool:
        """Check if Docker is available"""
        try:
            result = subprocess.run(
                ['docker', 'version'],
                capture_output=True,
                timeout=10
            )
            return result.returncode == 0
        except Exception:
            return False
    
    def pull_image(self, image: str) -> bool:
        """
        Pull Docker image if not available locally
        
        Args:
            image: Full image name (e.g., "alpine:latest")
            
        Returns:
            True if image is available
        """
        self.log(f"  Checking image availability: {image}")
        
        # Check if image exists locally
        try:
            result = subprocess.run(
                ['docker', 'image', 'inspect', image],
                capture_output=True,
                timeout=10
            )
            if result.returncode == 0:
                self.log(f"  → Image available locally")
                return True
        except Exception:
            pass
        
        # Try to pull image
        self.log(f"  → Pulling image (this may take a while)...")
        try:
            result = subprocess.run(
                ['docker', 'pull', image],
                capture_output=True,
                text=True,
                timeout=300  # 5 minutes for image pull
            )
            if result.returncode == 0:
                self.log(f"  → Image pulled successfully")
                return True
            else:
                self.log(f"  → Failed to pull image: {result.stderr[:200]}", "WARN")
                return False
        except subprocess.TimeoutExpired:
            self.log(f"  → Timeout pulling image", "WARN")
            return False
        except Exception as e:
            self.log(f"  → Error pulling image: {e}", "WARN")
            return False
    
    def discover_for_tool(self, tool: Dict) -> Optional[Dict]:
        """
        Discover binaries for a single tool
        
        Args:
            tool: Tool dictionary from config
            
        Returns:
            Discovery result dict or None if failed
        """
        tool_name = tool.get('name', 'Unknown')
        self.log(f"\n{'='*80}")
        self.log(f"Processing: {tool_name}")
        self.log(f"{'='*80}")
        
        # Check if tool has image_repo
        image_repo = tool.get('image_repo', {})
        if not image_repo or not image_repo.get('image'):
            self.log(f"  No image_repo defined, skipping", "WARN")
            return None
        
        # Get image and tag
        image_base = image_repo['image']
        image_tags = tool.get('image_tags', ['latest'])
        image_tag = 'latest' if 'latest' in image_tags else image_tags[0]
        docker_image = f"{image_base}:{image_tag}"
        
        self.log(f"  Image: {docker_image}")
        
        # Check image availability
        if not self.pull_image(docker_image):
            return {
                'status': 'failed',
                'reason': 'image_unavailable',
                'image': docker_image
            }
        
        # Discover binaries
        matches = BinaryFinder.discover_binaries_for_tool(docker_image, tool_name)
        
        if not matches:
            return {
                'status': 'failed',
                'reason': 'no_binaries_found',
                'image': docker_image
            }
        
        # Test each match to find working binaries
        working_binaries = []
        consecutive_failures = 0
        max_consecutive_failures = 3  # Stop after 3 consecutive failures
        min_confidence = 0.40  # Minimum confidence to consider (lowered to catch more valid binaries)
        
        for binary_path, match_type, confidence in matches[:10]:  # Test top 10 matches
            # Skip low confidence matches
            if confidence < min_confidence:
                self.log(f"  Skipping: {os.path.basename(binary_path)} (confidence {confidence:.2f} below threshold {min_confidence})")
                consecutive_failures += 1
                if consecutive_failures >= max_consecutive_failures:
                    break
                continue
            binary_name = os.path.basename(binary_path)
            self.log(f"  Testing: {binary_name} (confidence: {confidence:.2f}, type: {match_type})")
            
            # Test help command
            test_results = CommandExecutor.test_help_variations(binary_path, docker_image)
            
            if test_results['working_commands']:
                self.log(f"    ✓ Working help commands: {', '.join(test_results['working_commands'])}")
                working_binaries.append({
                    'path': binary_path,
                    'name': binary_name,
                    'confidence': confidence,
                    'match_type': match_type,
                    'help_command': test_results['best_command'],
                    'working_commands': test_results['working_commands']
                })
                consecutive_failures = 0  # Reset counter on success
            else:
                self.log(f"    ✗ No working help commands found")
                consecutive_failures += 1
                
                # Stop early if too many consecutive failures
                if consecutive_failures >= max_consecutive_failures:
                    self.log(f"    → Stopping after {consecutive_failures} consecutive failures")
                    break
        
        if not working_binaries:
            return {
                'status': 'partial',
                'reason': 'binary_found_no_help',
                'image': docker_image,
                'binaries_tested': len(matches[:10])
            }
        
        # Select primary binary (highest confidence with working help)
        primary = working_binaries[0]
        alternates = [b['name'] for b in working_binaries[1:] if b['name'] != primary['name']]
        
        self.log(f"\n  ✓ Discovery successful!")
        self.log(f"    Primary binary: {primary['name']}")
        self.log(f"    Help command: {primary['help_command']}")
        if alternates:
            self.log(f"    Alternate binaries: {', '.join(alternates[:5])}")
        
        return {
            'status': 'success',
            'binary': primary['name'],
            'alternate_binaries': alternates[:5],  # Limit to 5 alternates
            'help_command': primary['help_command'],
            'confidence': primary['confidence'],
            'match_type': primary['match_type'],
            'image': docker_image,
            'discovery_metadata': {
                'discovered_at': datetime.now().isoformat(),
                'method': primary['match_type'],
                'confidence': primary['confidence'],
                'verified': True
            }
        }
    
    def update_tool_config(self, tool: Dict, discovery_result: Dict):
        """
        Update tool configuration with discovery results
        
        Args:
            tool: Original tool dict
            discovery_result: Discovery result dict
        """
        if discovery_result['status'] == 'success':
            tool['binary'] = discovery_result['binary']
            tool['alternate_binaries'] = discovery_result['alternate_binaries']
            
            # Add discovery metadata to notes
            if 'notes' not in tool:
                tool['notes'] = ''
            
            note = f"Binary discovered automatically on {datetime.now().strftime('%Y-%m-%d')} " \
                   f"(method: {discovery_result['match_type']}, confidence: {discovery_result['confidence']:.2f})"
            
            if tool['notes']:
                tool['notes'] += f" | {note}"
            else:
                tool['notes'] = note
    
    def process_tools(
        self,
        only_tools: Optional[List[str]] = None,
        category: Optional[str] = None,
        limit: Optional[int] = None
    ):
        """
        Process tools and discover binaries
        
        Args:
            only_tools: If set, only process these specific tools
            category: If set, only process tools in this category
            limit: If set, limit number of tools to process
        """
        self.log("="*80)
        self.log("CLI Binary Discovery Tool")
        self.log("="*80)
        self.log(f"Config: {self.config_file}")
        self.log(f"Dry-run: {self.dry_run}")
        self.log(f"Timeout: 2 minutes per container scan")
        self.log("="*80)
        
        # Check Docker
        if not self.check_docker_available():
            self.log("Docker not available! Please install Docker.", "ERROR")
            return
        
        self.log("✓ Docker is available")
        
        # Load config
        if not self.load_config():
            return
        
        # Filter tools
        filtered_tools = []
        for tool in self.tools:
            # Skip if has binary already
            if tool.get('binary'):
                continue
            
            # Filter by category
            if category and tool.get('category') != category:
                continue
            
            # Filter by name
            if only_tools and tool.get('name') not in only_tools:
                continue
            
            # Must have image_repo
            if not tool.get('image_repo', {}).get('image'):
                continue
            
            filtered_tools.append(tool)
        
        if not filtered_tools:
            self.log("No tools to process after filtering", "WARN")
            return
        
        # Apply limit
        if limit:
            filtered_tools = filtered_tools[:limit]
        
        self.log(f"\nProcessing {len(filtered_tools)} tools")
        self.log("="*80)
        
        # Process each tool
        results = []
        for i, tool in enumerate(filtered_tools, 1):
            self.stats['total'] += 1
            
            self.log(f"\n[{i}/{len(filtered_tools)}]")
            
            result = self.discover_for_tool(tool)
            
            if result:
                results.append({
                    'tool': tool['name'],
                    **result
                })
                
                if result['status'] == 'success':
                    self.stats['success'] += 1
                    self.update_tool_config(tool, result)
                elif result['status'] == 'partial':
                    self.stats['partial'] += 1
                else:
                    self.stats['failed'] += 1
            else:
                self.stats['skipped'] += 1
                results.append({
                    'tool': tool['name'],
                    'status': 'skipped',
                    'reason': 'no_image_repo'
                })
        
        # Save config if changes were made
        if self.stats['success'] > 0:
            self.save_config()
        
        # Print summary
        self.print_summary(results)
    
    def print_summary(self, results: List[Dict]):
        """Print processing summary"""
        duration = (datetime.now() - self.stats['start_time']).total_seconds()
        
        self.log("\n" + "="*80)
        self.log("DISCOVERY SUMMARY")
        self.log("="*80)
        self.log(f"Duration: {duration:.1f}s ({duration/60:.1f} minutes)")
        self.log(f"Total processed: {self.stats['total']}")
        self.log(f"✓ Success: {self.stats['success']}")
        self.log(f"⚠ Partial: {self.stats['partial']} (binary found but help doesn't work)")
        self.log(f"✗ Failed: {self.stats['failed']}")
        self.log(f"⊙ Skipped: {self.stats['skipped']}")
        
        # Show successful discoveries
        successful = [r for r in results if r.get('status') == 'success']
        if successful:
            self.log("\n" + "="*80)
            self.log(f"SUCCESSFUL DISCOVERIES ({len(successful)})")
            self.log("="*80)
            for r in successful:
                self.log(f"  • {r['tool']:40s} → {r['binary']:20s} (confidence: {r.get('confidence', 0):.2f})")
        
        # Show failures
        failed = [r for r in results if r.get('status') in ['failed', 'partial']]
        if failed:
            self.log("\n" + "="*80)
            self.log(f"FAILED/PARTIAL ({len(failed)})")
            self.log("="*80)
            for r in failed:
                reason = r.get('reason', 'unknown')
                self.log(f"  • {r['tool']:40s} → {reason}")
        
        success_rate = (self.stats['success'] / self.stats['total'] * 100) if self.stats['total'] > 0 else 0
        self.log("\n" + "="*80)
        self.log(f"Success Rate: {success_rate:.1f}%")
        self.log("="*80)


def main():
    """CLI entry point"""
    parser = argparse.ArgumentParser(
        description='Discover binaries for CLI tools in Docker images',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Dry run to see what would be discovered
  python discover_binaries.py data/configs/cli_tools.json --dry-run
  
  # Discover and update config
  python discover_binaries.py data/configs/cli_tools.json --update
  
  # Process specific category
  python discover_binaries.py data/configs/cli_tools.json --category "Apache" --update
  
  # Process specific tools
  python discover_binaries.py data/configs/cli_tools.json --only "act" "Airflow" --update
  
  # Limit to first 10 tools
  python discover_binaries.py data/configs/cli_tools.json --limit 10 --update
        """
    )
    
    parser.add_argument('config', help='Path to cli_tools.json config file')
    parser.add_argument('--update', action='store_true', help='Update config file with discoveries')
    parser.add_argument('--dry-run', action='store_true', help='Dry run (no config updates)')
    parser.add_argument('--category', help='Only process tools in this category')
    parser.add_argument('--only', nargs='+', help='Only process these specific tools')
    parser.add_argument('--limit', type=int, help='Limit number of tools to process')
    
    args = parser.parse_args()
    
    # Determine dry-run mode
    dry_run = args.dry_run or not args.update
    
    if not args.update and not args.dry_run:
        print("Note: Running in dry-run mode. Use --update to save changes to config.")
        print()
    
    # Create and run discovery tool
    discovery = BinaryDiscoveryTool(args.config, dry_run=dry_run)
    discovery.process_tools(
        only_tools=args.only,
        category=args.category,
        limit=args.limit
    )


if __name__ == '__main__':
    main()


