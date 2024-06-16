import requests
import os
import subprocess
import json
import tarfile
import zipfile
from pymongo import MongoClient

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client.cli_archive

def download_and_extract(url, dest="/usr/local/bin"):
    if url.endswith('.tar.gz') or url.endswith('.tgz'):
        response = requests.get(url, stream=True)
        file_path = os.path.join(dest, "archive.tar.gz")
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        with tarfile.open(file_path, "r:gz") as tar:
            tar.extractall(path=dest)
    elif url.endswith('.zip'):
        response = requests.get(url, stream=True)
        file_path = os.path.join(dest, "archive.zip")
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(dest)
    else:
        response = requests.get(url, stream=True)
        file_path = os.path.join(dest, os.path.basename(url))
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        os.chmod(file_path, 0o755)
    return file_path

def call_help(binary, command=None):
    help_commands = [["--help"], ["-h"], ["help"]]
    for help_cmd in help_commands:
        cmd = [binary] + (command.split() if command else []) + help_cmd
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
    raise Exception(f"Failed to get help output for {binary} {' '.join(command)}")

def create_prompt_with_help_output(help_output):
    return (
        f"Identify the commands or subcommands presented in the following command-line tool help output "
        f"and store the result in a JSON list. Update the result to be a JSON list as the value of a 'subcommands' key "
        f"which contains each command/subcommand within a JSON object like {{'name': <command-name>, 'description': <command-description>}}. "
        f"Also do the same for the flags/options. The result should be a JSON list as a value for the 'options' key containing JSON objects "
        f"like {{'option': <option prefixed with '--'>, 'shortcut': <option shortcut prefixed with '-'>, 'description': <option-description>}}. "
        f"Ensure the result contains both subcommands and options for the output. If an option contains a string like '<EPOCH>' or 'value', store it as an optional property of the option object called 'value'. "
        f"Also, if an option contains a string like 'default: ', store the specified value as an optional property of the option object called 'default'. do the same for the following output though if the option belongs to or falls under a particular section like 'ETHEREUM OPTIONS' or 'LIGHT CLIENT OPTIONS', "
        f"add the section as an optional property called 'section' for the option JSON object. Also, include a top level description property for the JSON object which, based on the output, describes the root command being analyzed. "
        f"The sections should only be based on the output. Also update the JSON result with a top-level property called name with whatever the binary name is set to and sort both the subcommands and options lists in alphabetical order.\n\n{help_output}"
    )

def analyze_binary(binary, parent=None):
    help_output = call_help(binary, parent)
    prompt = create_prompt_with_help_output(help_output)
    
    headers = {
        'Authorization': f"Bearer {os.getenv('OPENAI_API_KEY')}",
        'Content-Type': 'application/json',
    }

    json_data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': prompt},
        ],
        'max_tokens': 150,
        'temperature': 0.7,
    }

    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=json_data)
        import pdb; pdb.set_trace()
        response.raise_for_status()
        result = json.loads(response.json()['choices'][0]['message']['content'].strip())
        result['name'] = f"{binary} {parent}" if parent else binary
        
        for command in result.get('commands', []):
            subcommand_name = command['name']
            subcommand_result = analyze_binary(binary, subcommand_name)
            command['subcommands'] = subcommand_result

        return result
    except requests.exceptions.RequestException as e:
        print(e.response.json() if e.response else str(e))
        return {'error': 'Failed to get answer'}

def main(binary_name, url=None):
    if url:
        binary_path = download_and_extract(url)
        binary_name = os.path.basename(binary_path)
    else:
        binary_path = binary_name

    result = analyze_binary(binary_path)
    # db.cli_archive.insert_one(result)
    print(f"Results for {binary_name} inserted into MongoDB")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="CLI Analyzer")
    parser.add_argument("binary_name", type=str, help="The name of the binary to analyze")
    parser.add_argument("--url", type=str, help="Optional URL to download the binary or archive file")

    args = parser.parse_args()
    main(args.binary_name, args.url)
