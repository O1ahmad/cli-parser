import argparse
import requests
import os
import subprocess
import json
import tarfile
import zipfile
from pymongo import MongoClient

# MongoDB setup
client = MongoClient("mongodb://dev:testing@localhost:27017/")
db = client.cli_archive

def download_file(url, dest):
    response = requests.get(url, stream=True)
    file_path = os.path.join(dest, os.path.basename(url))
    with open(file_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    return file_path

def extract_file(file_path, dest):
    if file_path.endswith(('.tar.gz', '.tgz')):
        with tarfile.open(file_path, "r:gz") as tar:
            tar.extractall(path=dest)
    elif file_path.endswith('.zip'):
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(dest)
    else:
        os.chmod(file_path, 0o755)
    return file_path

def download_and_extract(url, dest="/usr/local/bin"):
    """
    Downloads and extracts an archive file from the given URL to the specified destination.

    Args:
        url (str): The URL of the file to download.
        dest (str): The destination directory to extract the file to. Defaults to "/usr/local/bin".

    Returns:
        str: The file path of the downloaded and extracted file.
    """
    file_path = download_file(url, dest)
    return extract_file(file_path, dest)

def call_command(binary, commands):
    """
    Calls the specified command for the binary and returns the output.

    Args:
        binary (str): The name or path of the binary to call.
        commands (list): List of commands to try.

    Returns:
        str: The command output of the binary.

    Raises:
        Exception: If all attempts to get command output fail.
    """
    for command in commands:
        cmd = ([binary] if len(binary.split()) < 2 else binary.split()) + command
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
    raise Exception(f"Failed to get output for {binary} with commands {commands}")

def call_help(binary, command=None):
    return call_command(binary, [["--help"], ["-h"], ["help"]])

def call_version(binary):
    return call_command(binary, [["--version"], ["-v"], ["version"]])

def get_prompt(prompt_type):
    prompts = {
        "help": (
            f"Parse the command-line help output into a JSON with 'subcommands' and 'options'. "
            f"Subcommands can only begin with a lowercase letter; options start with '-' or '--'. "
            f"Subcommands: {{'name': <name>, 'description': <description>, 'usage': <usage>}}. "
            f"Options: {{'option': <'--option'>, 'shortcut': <'-shortcut'>, 'description': <description>, 'value': <value>, 'default': <default>, 'tags': [<tags>]}}. "
            f"Exclude missing properties. Include 'description' and 'name' for the root command. "
            f"Sort subcommands and options alphabetically. Include usage details for root and subcommands."
        ),
        "version": (
            f"Extract and return the version number (including commit SHAs) within a JSON object from the following version output."
        )
    }
    return prompts[prompt_type]

def analyze_output(binary, output, prompt_type):
    """
    Analyzes the output of a binary command and returns it in JSON format or plain text.

    Args:
        binary (str): The name or path of the binary to analyze.
        output (str): The output of the binary command.
        prompt_type (str): The type of prompt to use ('help' or 'version').

    Returns:
        dict or str: The parsed output in JSON format for help, or plain text for version.
    """
    prompt = get_prompt(prompt_type)
    headers = {
        'Authorization': f"Bearer {os.getenv('OPENAI_API_KEY')}",
        'Content-Type': 'application/json',
    }
    json_data = {
        'model': 'gpt-4o',
        'messages': [
            {'role': 'system', 'content': 'You are a helpful CLI parser assistant.'},
            {'role': 'user', 'content': prompt},
            {'role': 'user', 'content': output}
        ],
        'response_format': { 'type': "json_object" },
        'max_tokens': 4096,
        'temperature': 0.7,
    }

    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=json_data)
        response.raise_for_status()
        print("AI Token Usage:", response.json()['usage'])
        return response.json()['choices'][0]['message']['content'].strip()
    except requests.exceptions.RequestException as e:
        print(e.response.json() if e.response else str(e))
        return None

def analyze_binary_help(binary, parent=None):
    """
    Analyzes the help output of a binary and returns it in JSON format, including subcommands and options.

    Args:
        binary (str): The name or path of the binary to analyze.
        parent (str, optional): An additional command to append to the binary for deeper analysis. Defaults to None.

    Returns:
        dict: The parsed help output in JSON format, including subcommands and options.
    """
    print(f"Analyzing Binary: {binary}, Parent: {parent}")
    try:
        help_output = call_help(binary, parent)
    except Exception as e:
        print(str(e))
        return {'name': f"{binary} {parent}" if parent else binary, 'subcommands': [], 'options': []}

    result = analyze_output(binary, help_output, "help")
    if result:
        result = json.loads(result)
        result['name'] = f"{binary} {parent}" if parent else binary

        # Analyze subcommands recursively
        subcommands = []
        for command in result.get('subcommands', []):
            if command['name'].lower() not in ["help", (parent.lower() if parent else ""), binary]:
                subcommands.append(analyze_binary_help(result['name'], command['name']))
        result['subcommands'] = subcommands
        result['version'] = analyze_binary_version(binary)

        with open('result.json', 'a') as file:
            json.dump(result, file)
            file.write('\n')

        return result
    return {'name': f"{binary} {parent}" if parent else binary, 'subcommands': [], 'options': []}

def analyze_binary_version(binary):
    """
    Analyzes the version output of a binary and returns the version number.

    Args:
        binary (str): The name or path of the binary to analyze.

    Returns:
        str: The version number of the binary.
    """
    print(f"Analyzing Binary Version: {binary}")
    try:
        version_output = call_version(binary)
        return json.loads(analyze_output(binary, version_output, "version"))['version']
    except Exception as e:
        print(str(e))
        return None

def main(binary_name, url=None, save=False):
    """
    Main function to analyze a binary's help output and optionally save the results to MongoDB.

    Args:
        binary_name (str): The name of the binary to analyze.
        url (str, optional): URL to download the binary or archive file. Defaults to None.
        save (bool, optional): Whether to save the result to a local MongoDB instance. Defaults to False.
    """
    if url:
        binary_path = download_and_extract(url)
        binary_name = os.path.basename(binary_path)
    else:
        binary_path = binary_name

    result = analyze_binary_help(binary_path)
    print(result)
    if save:
        db.cli_archive.insert_one(result)
        print(f"Results for {binary_name} inserted into MongoDB")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI Analyzer")
    parser.add_argument("binary_name", type=str, help="The name of the binary to analyze")
    parser.add_argument("--url", type=str, help="Optional URL to download the binary or archive file")
    parser.add_argument("--save", action='store_true', help="Optionally save the result to a local MongoDB instance")

    args = parser.parse_args()
    main(args.binary_name, args.url, args.save)
