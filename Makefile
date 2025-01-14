# Variables
PACKAGE_NAME=cli_parser
DOCKER_IMAGE_NAME=cli_parser
PYTHON=python3
PIP=pip3
ARGS?=--help

# Targets
.PHONY: all build_image run_tests install_local run_script clean help

all: build_image run_tests install_local run_script

build_image:
	docker build -t $(DOCKER_IMAGE_NAME) .

run_tests:
	PYTHONPATH=src pytest tests/ --verbose

install_local:
	$(PIP) install .

run_script:
	$(PYTHON) -m src.parser $(ARGS)

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf build dist *.egg-info result.json

help:
	@echo "Makefile targets:"
	@echo "  all           - Build the Docker image, run tests, install package locally, and run the script"
	@echo "  build_image   - Build the Docker image from the Dockerfile"
	@echo "  run_tests     - Run the tests with pytest"
	@echo "  install_local - Install the package locally using pip"
	@echo "  run_script    - Run the parser script locally"
	@echo "  clean         - Remove temporary files and directories"
	@echo "  help          - Show this help message"
