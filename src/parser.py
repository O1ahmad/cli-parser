#!/usr/bin/env python3
"""
CLI Parser - Simplified, robust CLI documentation extractor

This parser reliably extracts help documentation from CLI tools whether running
in Docker containers or on the host system. It handles complex tools like AWS CLI
as well as simple tools like ls.
"""
import argparse
import json
import os
import sys
from typing import Dict, Optional

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(__file__))

from binary_finder import BinaryFinder
from command_executor import CommandExecutor


# AI Analysis imports
import requests


def analyze_with_ai(help_text: str, prompt_type: str = "help") -> Optional[Dict]:
    """
    Analyze help or version text using AI

    Args:
        help_text: The text to analyze
        prompt_type: Either "help" or "version"

    Returns:
        Parsed structure as dict, or None on failure
    """
    prompts = {
        "help": (
            "Parse command-line help output into JSON with 'subcommands', 'options', and 'aliases'. "
            "\n\nCRITICAL RULES:"
            "\n\n1. IDENTIFY COMMAND SECTIONS - Look for section headers that indicate commands, services, or groups:"
            "\n   - Sections containing words: 'Command', 'Commands', 'Service', 'Services', 'Group', 'Groups' (case-insensitive)"
            "\n   - Man page format: sections in all-caps ending with 'COMMANDS', 'SERVICES', 'GROUPS'"
            "\n   - Ignore text within parentheses in headers (e.g., 'Basic Commands (Beginner):' → section header only)"
            "\n"
            "\n2. EXTRACT SUBCOMMANDS - From identified sections, extract ONLY the indented/listed items:"
            "\n   RULES:"
            "\n   - Extract the FIRST WORD from each indented line as the subcommand name"
            "\n   - Indented lines have leading whitespace (spaces or tabs)"
            "\n   - Strip special characters: 'buildx*' → 'buildx', '+o service' → 'service', '- item' → 'item'"
            "\n   - Include the description (remaining text on the same line after the command name)"
            "\n   - NEVER extract words from the section header line itself - only from indented items below it"
            "\n"
            "\n3. EXTRACT OPTIONS - Items starting with '-' or '--' in sections like 'Options:', 'Flags:', 'Global Options:'"
            "\n"
            "\n4. EXTRACT ALIASES - Only from 'Aliases:' sections (these are alternative names, NOT subcommands)"
            "\n"
            "\n5. EXCLUDE from subcommands:"
            "\n   - Section header lines (lines ending with ':' without leading whitespace)"
            "\n   - Text within parentheses in section headers"
            "\n   - Items in 'Arguments:', 'Positional Arguments:', 'Usage:', 'Examples:' sections"
            "\n   - Resource type abbreviations like 'pod (po)', 'service (svc)'"
            "\n   - Anything starting with '-' or '--' (these are options, not subcommands)"
            "\n   - All-caps section headers: 'DESCRIPTION', 'SYNOPSIS', 'EXAMPLES'"
            "\n"
            "\n6. COMPLETENESS - Extract ALL items from all command/service/group sections. Do not stop early."
            "\n\nOUTPUT FORMAT (JSON):"
            "\n{"
            '\n  "subcommands": [{"name": "cmd", "description": "desc"}, ...],'
            '\n  "options": [{"option": "--flag", "shortcut": "-f", "description": "desc", "value": "val", "default": "def"}, ...],'
            '\n  "aliases": ["alias1", "alias2", ...]'
            "\n}"
        ),
        "version": "Extract version number from the output and return as JSON: {'version': <version_string>}"
    }

    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("Warning: OPENAI_API_KEY not set, skipping AI analysis")
        return None

    headers = {
        'Authorization': f"Bearer {api_key}",
        'Content-Type': 'application/json',
    }

    json_data = {
        'model': 'gpt-4o-mini',
        'messages': [
            {'role': 'system', 'content': 'You are a CLI parser that returns JSON.'},
            {'role': 'user', 'content': prompts[prompt_type]},
            {'role': 'user', 'content': help_text}
        ],
        'response_format': {'type': "json_object"},
        'temperature': 0.7,
    }

    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=json_data,
            timeout=300  # 5 minutes for large help texts like AWS CLI
        )
        response.raise_for_status()

        content = response.json()['choices'][0]['message']['content']
        return json.loads(content)

    except Exception as e:
        print(f"AI analysis error: {e}")
        return None


def parse_command(binary_path: str, parent_command: Optional[str], docker_image: Optional[str],
                 depth: int, max_depth: int, parent_help_text: Optional[str] = None) -> Dict:
    """
    Recursively parse a command and its subcommands

    Args:
        binary_path: Full path to the binary
        parent_command: Parent command string (e.g., "config" for "git config")
        docker_image: Optional Docker image to run in
        depth: Current recursion depth
        max_depth: Maximum recursion depth
        parent_help_text: Help text from parent command for comparison

    Returns:
        Parsed command structure as dict
    """
    # Build display name
    binary_name = os.path.basename(binary_path)
    if parent_command:
        display_name = f"{binary_name} {parent_command}"
    else:
        display_name = binary_name

    print(f"\n[Depth {depth}] Analyzing: {display_name}")

    # Stop recursion if max depth reached
    if depth >= max_depth:
        print(f"  → Max depth {max_depth} reached, stopping recursion")
        return {'name': display_name, 'subcommands': [], 'options': [], 'aliases': []}

    # Get help text
    help_text = CommandExecutor.execute_help(binary_path, parent_command, docker_image)

    if not help_text:
        print(f"  → No help text retrieved")
        return {'name': display_name, 'subcommands': [], 'options': [], 'aliases': []}

    # Check if help text is identical to parent (indicates resource type, not real subcommand)
    if parent_help_text and help_text == parent_help_text:
        print(f"  → Help text identical to parent (likely a resource type, not a subcommand)")
        return {'name': display_name, 'subcommands': [], 'options': [], 'aliases': []}

    print(f"  → Help text retrieved ({len(help_text)} chars)")
    print(f"  → Full help text:")
    preview = help_text.replace('\n', '\n     ')
    print(f"     {preview}")

    # Parse with AI
    parsed = analyze_with_ai(help_text, "help")

    if not parsed:
        print(f"  → AI parsing failed")
        return {'name': display_name, 'subcommands': [], 'options': [], 'aliases': [], 'raw_help_text': help_text}

    # Add metadata
    parsed['name'] = display_name
    parsed['raw_help_text'] = help_text

    # Ensure required fields exist
    if 'subcommands' not in parsed:
        parsed['subcommands'] = []
    if 'options' not in parsed:
        parsed['options'] = []
    if 'aliases' not in parsed:
        parsed['aliases'] = []

    num_subcmds = len(parsed['subcommands'])
    num_opts = len(parsed['options'])
    num_aliases = len(parsed['aliases'])

    print(f"  → Extracted: {num_subcmds} subcommands, {num_opts} options, {num_aliases} aliases")

    # Show first few subcommands and options
    if num_subcmds > 0:
        print(f"  → First subcommands: {', '.join([s['name'] for s in parsed['subcommands'][:5]])}{' ...' if num_subcmds > 5 else ''}")
    if num_opts > 0:
        print(f"  → First options: {', '.join([o.get('option', o.get('shortcut', '?')) for o in parsed['options'][:5]])}{' ...' if num_opts > 5 else ''}")

    # Recursively parse subcommands
    if num_subcmds > 0 and depth < max_depth:
        aliases_lower = [a.lower() for a in parsed['aliases']]
        processed_subcommands = []

        # Build set of words in current command path for redundancy checking
        current_path_words = set()
        if parent_command:
            current_path_words = {w.lower() for w in parent_command.split()}
        current_path_words.add(os.path.basename(binary_path).lower())

        for subcmd in parsed['subcommands']:
            subcmd_name = subcmd.get('name', '')

            # Skip if it's an alias
            if subcmd_name.lower() in aliases_lower:
                print(f"  → Skipping '{subcmd_name}' (it's an alias)")
                continue

            # Skip help commands
            if subcmd_name.lower() in ['help', 'h', '--help', '-h']:
                continue

            # Check for redundant words in subcommand name
            subcmd_words = [w.lower() for w in subcmd_name.split()]
            redundant_words = [w for w in subcmd_words if w in current_path_words]

            if redundant_words:
                print(f"  → Skipping '{subcmd_name}' (redundant words: {redundant_words})")
                continue

            # Check for repeated words within the subcommand itself
            if len(subcmd_words) != len(set(subcmd_words)):
                print(f"  → Skipping '{subcmd_name}' (contains repeated words)")
                continue

            # Build next parent command
            if parent_command:
                next_parent = f"{parent_command} {subcmd_name}"
            else:
                next_parent = subcmd_name

            # Recursively parse
            subcmd_parsed = parse_command(
                binary_path,
                next_parent,
                docker_image,
                depth + 1,
                max_depth,
                help_text  # Pass current help text for comparison
            )

            # Skip subcommands that failed to retrieve help text (likely invalid commands)
            # Check if it has no help text and no valid content
            has_content = (
                subcmd_parsed.get('subcommands') or
                subcmd_parsed.get('options') or
                subcmd_parsed.get('raw_help_text')
            )
            if not has_content:
                print(f"  → Skipping '{subcmd_name}' (no help text retrieved - likely invalid command)")
                continue

            # Preserve original description
            if 'description' not in subcmd_parsed and 'description' in subcmd:
                subcmd_parsed['description'] = subcmd['description']

            processed_subcommands.append(subcmd_parsed)

        parsed['subcommands'] = processed_subcommands

    return parsed


def parse_binary(binary_name: str, docker_image: Optional[str] = None,
                max_depth: int = 20) -> Optional[Dict]:
    """
    Main entry point: parse a binary and extract all documentation

    Args:
        binary_name: Name or path of binary to parse
        docker_image: Optional Docker image to run in
        max_depth: Maximum recursion depth for subcommands

    Returns:
        Complete parsed structure as dict, or None on failure
    """
    print(f"\n{'='*80}")
    print(f"Parsing: {binary_name}")
    if docker_image:
        print(f"Docker Image: {docker_image}")
    print(f"Max Depth: {max_depth}")
    print(f"{'='*80}")

    # Find binary path
    if docker_image:
        binary_path, method = BinaryFinder.find_in_container(docker_image, binary_name)
        if not binary_path:
            print(f"\n✗ Binary '{binary_name}' not found in container")
            return None
        print(f"\n✓ Binary found in container: {binary_path}")
        print(f"  Search method: {method}")
    else:
        # Check if it's already a full path
        if binary_name.startswith('/'):
            binary_path = binary_name
            method = "provided-as-path"
        else:
            binary_path, method = BinaryFinder.find_on_host(binary_name)
            if not binary_path:
                print(f"\n✗ Binary '{binary_name}' not found on host")
                return None

        print(f"\n✓ Binary found on host: {binary_path}")
        print(f"  Search method: {method}")

    # Parse the binary recursively
    result = parse_command(binary_path, None, docker_image, depth=0, max_depth=max_depth)

    # Get version
    print(f"\nGetting version information...")
    version_text = CommandExecutor.execute_version(binary_path, docker_image)

    if version_text:
        print(f"  → Version text retrieved ({len(version_text)} chars)")
        version_parsed = analyze_with_ai(version_text, "version")
        if version_parsed and 'version' in version_parsed:
            result['version'] = version_parsed['version']
            print(f"  → Version: {result['version']}")
        else:
            result['version'] = None
            print(f"  → Could not parse version")
    else:
        result['version'] = None
        print(f"  → No version text retrieved")

    return result


def main():
    """CLI entry point"""
    arg_parser = argparse.ArgumentParser(
        description='Parse CLI tool documentation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Parse local binary
  python parser.py ls --max-depth 1

  # Parse in Docker
  python parser.py doctl --docker docker.io/digitalocean/doctl:latest

  # Parse with output file
  python parser.py kubectl --docker bitnami/kubectl:latest --output kubectl.json
        """
    )

    arg_parser.add_argument('binary', help='Binary name or path to parse')
    arg_parser.add_argument('--docker', help='Docker image to run binary in')
    arg_parser.add_argument('--max-depth', type=int, default=20, help='Maximum recursion depth (default: 20)')
    arg_parser.add_argument('--output', '-o', help='Output JSON file (default: stdout)')

    args = arg_parser.parse_args()

    # Parse the binary
    result = parse_binary(args.binary, args.docker, args.max_depth)

    if not result:
        print("\n✗ Parsing failed")
        sys.exit(1)

    # Output results
    json_output = json.dumps(result, indent=2)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(json_output)
        print(f"\n✓ Results written to: {args.output}")
    else:
        print("\n" + "="*80)
        print("RESULTS:")
        print("="*80)
        print(json_output)

    print(f"\n✓ Parsing complete")


if __name__ == '__main__':
    main()
