import unittest
from unittest.mock import patch
from cli_parser.parser import parse_cli_command
import subprocess

class TestCLIParser(unittest.TestCase):
    
    @patch('subprocess.run')
    def test_parse_aws(self, mock_subprocess_run):
        aws_help_output = """
        aws

        Usage: aws [options] [command] [command options]

        Available Commands:
        ec2         EC2 service
        s3          S3 service
        configure   Configure AWS CLI
        """
        
        aws_ec2_help_output = """
        aws ec2

        Usage: aws ec2 [options] [command] [command options]

        Available Commands:
        describe-instances    Describe EC2 instances
        start-instances       Start EC2 instances
        stop-instances        Stop EC2 instances
        """
        
        aws_s3_help_output = """
        aws s3

        Usage: aws s3 [options] [command] [command options]

        Available Commands:
        ls                    List S3 buckets
        cp                    Copy files
        """
        
        mock_subprocess_run.side_effect = [
            subprocess.CompletedProcess(args='aws --help', returncode=0, stdout=aws_help_output),
            subprocess.CompletedProcess(args='aws ec2 --help', returncode=0, stdout=aws_ec2_help_output),
            subprocess.CompletedProcess(args='aws s3 --help', returncode=0, stdout=aws_s3_help_output)
        ]
        
        expected_output = {
            "aws": {
                "ec2": {
                    "describe-instances": {"flags": []},
                    "start-instances": {"flags": []},
                    "stop-instances": {"flags": []}
                },
                "s3": {
                    "ls": {"flags": []},
                    "cp": {"flags": []}
                },
                "configure": {"flags": []}
            }
        }
        
        self.assertEqual(parse_cli_command("aws"), expected_output)

    @patch('subprocess.run')
    def test_parse_docker(self, mock_subprocess_run):
        docker_help_output = """
        docker

        Usage: docker [OPTIONS] COMMAND [ARGS...]

        A self-sufficient runtime for containers

        Options:
        --config string      Location of client config files
        -D, --debug          Enable debug mode
        --help               Print usage

        Management Commands:
        container    Manage containers
        image        Manage images
        """
        
        docker_container_help_output = """
        docker container

        Usage: docker container COMMAND

        Manage containers
        """

        docker_image_help_output = """
        docker container

        Usage: docker image COMMAND

        Manage images
        """
        
        mock_subprocess_run.side_effect = [
            subprocess.CompletedProcess(args='docker --help', returncode=0, stdout=docker_help_output),
            subprocess.CompletedProcess(args='docker container --help', returncode=0, stdout=docker_container_help_output),
            subprocess.CompletedProcess(args='docker image --help', returncode=0, stdout=docker_image_help_output)
        ]
        
        expected_output = {
            "docker": {
                "container": {
                    "ls": {"flags": []},
                    "run": {"flags": []}
                },
                "image": {"flags": []},
                "volume": {"flags": []},
                "network": {"flags": []},
                "flags": [
                    {"shortcut": None, "flag": "--config string", "description": "Location of client config files"},
                    {"shortcut": "-D", "flag": "--debug", "description": "Enable debug mode"},
                    {"shortcut": None, "flag": "--help", "description": "Print usage"}
                ]
            }
        }
        
        self.assertEqual(parse_cli_command("docker"), expected_output)

if __name__ == '__main__':
    unittest.main()
