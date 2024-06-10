import os
import subprocess
import re
import requests
import tarfile
import zipfile
import shutil
import argparse

def execute_command(command, args):
    try:
        full_command = f"{command} {args}"
        result = subprocess.run(full_command.split(), shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError:
        return None

def execute_help_command(command):
    """
    Executes the given command with --help, -h, or help and returns the output.
    """
    help_args = ["--help"]
    for arg in help_args:
        output = execute_command(command, arg)
        if output is not None:
            return output
    return None

def parse_cli_command(command):
    result = execute_help_command(command)
    
    if result is None:
        return {"error": "Command execution failed"}

    subcommands, flags = parse_help_output(command, result)
    command_parts = command.split()
    if subcommands:
        subcommand_dict = {}
        for subcommand in subcommands:
            full_subcommand = f"{command} {subcommand}"
            subcommand_dict[subcommand] = parse_cli_command(full_subcommand)
        return {command_parts[-1]: subcommand_dict}
    else:
        return {command_parts[-1]: {"flags": flags}}

def parse_help_output(command, output):
    subcommands = []
    flags = []
    
    subcommand_pattern = re.compile(r'^\s*([a-z][\w.-]*)\s+(.+)$')
    flag_pattern = re.compile(r'^\s*(?P<shortcut>-\w,?\s*)?(?P<flag>--\w+)?(?:\s+(?P<description>.+))?')
    
    for line in output.splitlines():
        if not line.strip():
            continue  # Ignore empty lines and lines with only whitespace
        
        subcommand_match = subcommand_pattern.match(line)
        flag_match = flag_pattern.match(line)
        
        if subcommand_match:
            subcommand = subcommand_match.group(1)
            full_subcommand = f"{command} {subcommand}"
            if execute_help_command(full_subcommand) is not None:
                subcommands.append(subcommand)
        elif flag_match and (flag_match.group('shortcut') or flag_match.group('flag')):
            flag_info = {
                "shortcut": flag_match.group('shortcut').strip() if flag_match.group('shortcut') else None,
                "flag": flag_match.group('flag').strip() if flag_match.group('flag') else None,
                "description": flag_match.group('description').strip()
            }
            flags.append(flag_info)

    return subcommands, flags

def download_and_install_binary(command, version, url, install_path='/usr/local/bin'):
    """
    Downloads a binary or archive from the given URL and installs it to the specified location.
    """
    # Create a temporary directory to download and extract files
    temp_dir = "/tmp/cli_parser_temp"
    os.makedirs(temp_dir, exist_ok=True)
    
    # Download the file
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        file_name = url.split('/')[-1]
        file_path = os.path.join(temp_dir, file_name)
        with open(file_path, 'wb') as f:
            f.write(response.content)
    else:
        raise Exception(f"Failed to download file from {url}")

    # Determine if the file is an archive and extract if necessary
    if tarfile.is_tarfile(file_path):
        with tarfile.open(file_path, 'r:*') as tar:
            tar.extractall(path=temp_dir)
    elif zipfile.is_zipfile(file_path):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
    else:
        # If it's not an archive, assume it's the binary itself
        extracted_files = [file_path]
    
    # Find the binary file (assuming it is the command name)
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            if file == command or file.startswith(command):
                extracted_files = [os.path.join(root, file)]
                break

    # Move the binary to the specified installation path
    if not os.path.exists(install_path):
        os.makedirs(install_path, exist_ok=True)
        
    for file in extracted_files:
        shutil.move(file, os.path.join(install_path, command))
        os.chmod(os.path.join(install_path, command), 0o755)
    
    # Clean up temporary directory
    shutil.rmtree(temp_dir)
    
    print(f"{command} {version} installed successfully at {install_path}")

def main():
    parser = argparse.ArgumentParser(description='CLI Parser')
    parser.add_argument('command', help='Command to parse')
    parser.add_argument('--version', '-v', help='Version of the command')
    parser.add_argument('--url', '-u', help='URL to download the binary')

    args = parser.parse_args()

    if args.version and not args.url:
        parser.error("--version requires --url")
    if args.url and not args.version:
        parser.error("--url requires --version")

    command = args.command
    version = args.version
    url = args.url

    if version and url:
        download_and_install_binary(command, version, url)
    else:
        result = parse_cli_command(command)
        print(result)

if __name__ == "__main__":
    main()
