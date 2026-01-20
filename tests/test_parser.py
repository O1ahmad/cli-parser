import json
import subprocess
from unittest.mock import MagicMock, patch

import pytest

from src.parser import parse_binary


@pytest.fixture
def mock_subprocess_run():
    with patch("subprocess.run") as mock_run:
        yield mock_run


def compare_dicts(result, expected):
    """
    Recursively compares two dictionaries and asserts that all expected keys match.
    Ignores extra keys in result (like raw_help_text, version).

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
    """Test parsing AWS CLI with mocked subprocess and OpenAI API calls"""
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
        # which aws
        subprocess.CompletedProcess(args=["which", "aws"], returncode=0, stdout="/usr/local/bin/aws\n", stderr=""),
        # aws --help
        subprocess.CompletedProcess(args=["aws", "--help"], returncode=0, stdout=aws_help_output, stderr=""),
        # aws ec2 --help
        subprocess.CompletedProcess(args=["aws", "ec2", "--help"], returncode=0, stdout=aws_ec2_help_output, stderr=""),
        # aws ec2 describe-instances --help
        subprocess.CompletedProcess(
            args=["aws", "ec2", "describe-instances", "--help"],
            returncode=0,
            stdout=aws_ec2_describe_instances_help_output,
            stderr="",
        ),
        # aws ec2 describe-instances --version attempts (all fail)
        subprocess.CompletedProcess(
            args=["aws", "ec2", "describe-instances", "--version"], returncode=1, stdout="", stderr=""
        ),
        subprocess.CompletedProcess(
            args=["aws", "ec2", "describe-instances", "-v"], returncode=1, stdout="", stderr=""
        ),
        subprocess.CompletedProcess(
            args=["aws", "ec2", "describe-instances", "version"], returncode=1, stdout="", stderr=""
        ),
        # aws s3 --help
        subprocess.CompletedProcess(args=["aws", "s3", "--help"], returncode=0, stdout=aws_s3_help_output, stderr=""),
        # aws s3 ls --help
        subprocess.CompletedProcess(
            args=["aws", "s3", "ls", "--help"], returncode=0, stdout=aws_s3_ls_help_output, stderr=""
        ),
        # aws s3 ls --version attempts (all fail)
        subprocess.CompletedProcess(args=["aws", "s3", "ls", "--version"], returncode=1, stdout="", stderr=""),
        subprocess.CompletedProcess(args=["aws", "s3", "ls", "-v"], returncode=1, stdout="", stderr=""),
        subprocess.CompletedProcess(args=["aws", "s3", "ls", "version"], returncode=1, stdout="", stderr=""),
        # aws --version (main version)
        subprocess.CompletedProcess(args=["aws", "--version"], returncode=0, stdout="aws-cli/2.0.0", stderr=""),
    ]

    expected_output = {
        "name": "aws",
        "subcommands": [
            {
                "name": "aws ec2",
                "description": "EC2 service",
                "subcommands": [
                    {
                        "name": "aws ec2 describe-instances",
                        "description": "Describe EC2 instances",
                        "options": [{"option": "--filters", "description": "Filters to apply to the request"}],
                        "subcommands": [],
                        "aliases": [],
                    }
                ],
                "options": [],
                "aliases": [],
            },
            {
                "name": "aws s3",
                "description": "S3 service",
                "subcommands": [
                    {
                        "name": "aws s3 ls",
                        "description": "List S3 buckets",
                        "options": [{"option": "--profile", "description": "Specify the profile to use"}],
                        "subcommands": [],
                        "aliases": [],
                    }
                ],
                "options": [],
                "aliases": [],
            },
        ],
        "options": [],
        "aliases": [],
    }

    # Mock OpenAI API responses
    def mock_openai_response(*args, **kwargs):
        """Mock OpenAI API calls based on the input"""
        response = MagicMock()
        response.raise_for_status = MagicMock()

        # Extract the help text from the request
        help_text = kwargs["json"]["messages"][-1]["content"]

        # Determine which response to return based on the help text
        if "AWS CLI tool" in help_text and "Available Commands:" in help_text and "ec2" in help_text:
            # Main aws help
            ai_response = {
                "subcommands": [
                    {"name": "ec2", "description": "EC2 service"},
                    {"name": "s3", "description": "S3 service"},
                ],
                "options": [],
                "aliases": [],
            }
        elif "EC2 service" in help_text and "describe-instances" in help_text:
            # aws ec2 help
            ai_response = {
                "subcommands": [{"name": "describe-instances", "description": "Describe EC2 instances"}],
                "options": [],
                "aliases": [],
            }
        elif (
            "Describe EC2 instances" in help_text and "--filters" in help_text and "Available Commands" not in help_text
        ):
            # aws ec2 describe-instances help
            ai_response = {
                "subcommands": [],
                "options": [{"option": "--filters", "description": "Filters to apply to the request"}],
                "aliases": [],
            }
        elif "S3 service" in help_text and "ls" in help_text:
            # aws s3 help
            ai_response = {
                "subcommands": [{"name": "ls", "description": "List S3 buckets"}],
                "options": [],
                "aliases": [],
            }
        elif "List S3 buckets" in help_text and "--profile" in help_text:
            # aws s3 ls help
            ai_response = {
                "subcommands": [],
                "options": [{"option": "--profile", "description": "Specify the profile to use"}],
                "aliases": [],
            }
        elif "aws-cli/2.0.0" in help_text:
            # Version response
            ai_response = {"version": "2.0.0"}
        else:
            # Default empty response
            ai_response = {"subcommands": [], "options": [], "aliases": []}

        response.json.return_value = {"choices": [{"message": {"content": json.dumps(ai_response)}}]}
        return response

    with patch("requests.post", side_effect=mock_openai_response):
        result = parse_binary("aws")
        compare_dicts(result, expected_output)
