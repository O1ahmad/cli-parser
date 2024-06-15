import re
import subprocess
import argparse
import json


def get_binary_help_text(binary_name):
    commands = [['--help'], ['-h'], ['help']]
    for cmd in commands:
        try:
            result = subprocess.run([binary_name] + cmd, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError:
            continue
        except subprocess.SubprocessError as e:
            print(f"Error running '{binary_name} {cmd}': {e}")
            return None
    return None

def parse_options(help_text):
    # Regex pattern to match options and descriptions
    pattern = r'''
      ^\s*(?P<shortcut>\s*-\w+)?(?:,\s*)?  # shortcut (optional comma and whitespace)
  (?P<flag>\s*--[\w.-]+)?         # flag
  \s*
  (?P<description>.*)?            # description
    '''
    
    # Compile the regex pattern
    regex = re.compile(pattern, re.VERBOSE | re.MULTILINE)
    
    # Find all matches in the text
    matches = regex.finditer(help_text)
    
    # List to store matched options
    options_list = []
    
    # Iterate through matches
    for match in matches:
        option_dict = match.groupdict()
        # Strip leading/trailing whitespace from shortcut, flag, and description
        option_dict['shortcut'] = option_dict['shortcut'].strip() if option_dict['shortcut'] else None
        option_dict['flag'] = option_dict['flag'].strip() if option_dict['flag'] else None
        option_dict['description'] = option_dict['description'].strip() if option_dict['description'] else None

        if option_dict['shortcut'] or option_dict['flag']:
            options_list.append(option_dict)
    
    return options_list

def main(binary_name):
    # Get help text from the binary
    help_text = get_binary_help_text(binary_name)
    
    if help_text:
        # Parse options from help text
        options_list = parse_options(help_text)
        
        if options_list:
            # Convert the list of dictionaries to JSON format
            options_json = json.dumps(options_list, indent=2)
            
            # Print the JSON output
            print(options_json)
        else:
            print(f"No options found in the help text of '{binary_name}'.")
    else:
        print(f"Failed to retrieve help text from '{binary_name}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse options from a binary\'s help output')
    parser.add_argument('binary_name', type=str, help='Name of the binary to parse help from')
    
    args = parser.parse_args()
    main(args.binary_name)

