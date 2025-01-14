import pytest
from unittest.mock import patch
import subprocess
from src.parser import main


@pytest.fixture
def mock_subprocess_run():
    with patch('subprocess.run') as mock_run:
        yield mock_run

def compare_dicts(result, expected):
    """
    Recursively compares two dictionaries and asserts that all raw values are equal.

    Args:
        result (dict): The dictionary obtained from the function.
        expected (dict): The expected dictionary to compare against.

    Raises:
        AssertionError: If any key-value pair does not match.
    """
    for key in expected:
        assert key in result, f"Key '{key}' missing in result."
        if isinstance(expected[key], dict):
            assert isinstance(result[key], dict), f"Key '{key}' is not a dictionary in result."
            compare_dicts(result[key], expected[key])  # Recursive call
        elif isinstance(expected[key], list):
            assert isinstance(result[key], list), f"Key '{key}' is not a list in result."
            assert len(result[key]) == len(expected[key]), f"List lengths for key '{key}' do not match."
            for res_item, exp_item in zip(result[key], expected[key]):
                if isinstance(exp_item, dict):
                    compare_dicts(res_item, exp_item)  # Recursive call for list of dicts
                else:
                    assert res_item == exp_item, f"Mismatch in list value for key '{key}': {res_item} != {exp_item}"
        else:
            assert result[key] == expected[key], f"Value mismatch for key '{key}': {result[key]} != {expected[key]}"

def test_parse_aws(mock_subprocess_run):
    # Mock outputs for aws commands
    aws_help_output = """
    AWS CLI tool for managing Amazon Web Services

    Usage: aws [options] [command] [command options]

    Available Commands:
    ec2         EC2 service
    s3          S3 service
    """
    
    aws_ec2_help_output = """
    EC2 service

    Usage: aws ec2 [options] [command] [command options]

    Available Commands:
    describe-instances    Describe EC2 instances
    """
    
    aws_ec2_describe_instances_help_output = """
    Describe EC2 instances

    Usage: aws ec2 describe-instances [options]

    Options:
    --filters   Filters to apply to the request
    """
    
    aws_s3_help_output = """
    S3 service

    Usage: aws s3 [options] [command] [command options]

    Available Commands:
    ls                    List S3 buckets
    """
    
    aws_s3_ls_help_output = """
    List S3 buckets

    Usage: aws s3 ls [options]

    Options:
    --profile   Specify the profile to use
    """

    # Define the side effects for subprocess.run
    mock_subprocess_run.side_effect = [
        subprocess.CompletedProcess(args='aws --help', returncode=0, stdout=aws_help_output),
        subprocess.CompletedProcess(args='aws ec2 --help', returncode=0, stdout=aws_ec2_help_output),
        subprocess.CompletedProcess(args='aws ec2 describe-instances --help', returncode=0, stdout=aws_ec2_describe_instances_help_output),
        subprocess.CompletedProcess(args='aws s3 --help', returncode=0, stdout=aws_s3_help_output),
        subprocess.CompletedProcess(args='aws s3 ls --help', returncode=0, stdout=aws_s3_ls_help_output),
    ]
    
    expected_output = {
        'name': 'aws',
        'description': 'AWS CLI tool for managing Amazon Web Services',
        'usage': 'aws [options] [command] [command options]',
        'subcommands': [
            {
                'name': 'aws ec2',
                'description': 'EC2 service',
                'usage': 'aws ec2 [options] [command] [command options]',
                'subcommands': [
                    {
                        'name': 'aws ec2 describe-instances',
                        'description': 'Describe EC2 instances',
                        'usage': 'aws ec2 describe-instances [options]',
                        'options': [
                            {
                                'option': '--filters',
                                'description': 'Filters to apply to the request'
                            }
                        ],
                        'subcommands': []
                    }
                ],
                'options': []
            },
            {
                'name': 'aws s3',
                'description': 'S3 service',
                'usage': 'aws s3 [options] [command] [command options]',
                'subcommands': [
                    {
                        'name': 'aws s3 ls',
                        'description': 'List S3 buckets',
                        'usage': 'aws s3 ls [options]',
                        'options': [
                            {
                                'option': '--profile',
                                'description': 'Specify the profile to use'
                            }
                        ],
                        'subcommands': []
                    }
                ],
                'options': []
            }
        ],
    }
    
    result = main("aws")
    compare_dicts(result, expected_output)
