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
        cmd = ([binary] if len(binary.split()) < 2 else binary.split()) + (command.split() if command else []) + help_cmd
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
    raise Exception(f"Failed to get help output for {binary} {' '.join(command)}")

def get_help_output_prompt():
    return (
        f"Parse the command-line tool help output into a JSON object with 'subcommands' and 'options' keys. "
        f"Subcommands start with a lowercase alphanumeric character; options start with '-' or '--'. "
        f"Subcommands format: {{'name': <name>, 'description': <description>}}. "
        f"Options format: {{'option': <'--option'>, 'shortcut': <'-shortcut'>, 'description': <description>, 'value': <value>, 'default': <default>, 'section': <section>}}. "
        f"Include 'description' for the root command and 'name' for the binary. Sort subcommands and options alphabetically."
    )

def analyze_binary_help(binary, parent=None):
    try:
        help_output = call_help(binary, parent)
    except Exception as e:
        print(str(e))
        return {
            'name': f"{binary} {parent}" if parent else binary,
            'subcommands': [],
            'options': []
        }

    prompt = get_help_output_prompt()
    headers = {
        'Authorization': f"Bearer {os.getenv('OPENAI_API_KEY')}",
        'Content-Type': 'application/json',
    }
    json_data = {
        'model': 'gpt-4o',
        'messages': [
            {'role': 'system', 'content': 'You are a helpful CLI parser assistant who parses command-line output and returns results in well-formatted JSON.'},
            {'role': 'user', 'content': prompt},
            {'role': 'user', 'content': help_output}
        ],
        'response_format': { 'type': "json_object" },
        'max_tokens': 4096,
        'temperature': 0.7,
    }

    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=json_data)
        response.raise_for_status()

        print("AI Token Usage:", response.json()['usage'])
        result = json.loads(response.json()['choices'][0]['message']['content'].strip())
        result['name'] = f"{binary} {parent}" if parent else binary

        # Analyze subcommands recursively
        subcommands = []
        for command in result.get('subcommands', []):
            if (command['name'].lower() == "help"):
                continue

            subcommand_name = command['name']
            subcommand_result = analyze_binary_help(result['name'], subcommand_name)
            subcommands.append(subcommand_result)

        result['subcommands'] = subcommands

        # Write result to file
        with open('result.json', 'a') as file:
            json.dump(result, file)
            file.write('\n')

        return result

    except requests.exceptions.RequestException as e:
        print(e.response.json() if e.response else str(e))
        return {'error': 'Failed to get answer'}
    except Exception as e:
        print(str(e))
        print(f"{binary} {parent}" if parent else binary)
        return {
            'name': f"{binary} {parent}" if parent else binary,
            'subcommands': [],
            'options': []
        }

def main(binary_name, url=None, save=None):
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
    parser.add_argument("--save", type=bool, help="Optionally save the result to a local MongoDB instance")

    args = parser.parse_args()
    main(args.binary_name, args.url, args.save)
