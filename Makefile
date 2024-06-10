# Variables
PACKAGE_NAME=cli_parser
DOCKER_IMAGE_NAME=cli_parser_image
PYTHON=python3
PIP=pip3

# Targets
.PHONY: all build_image run_tests install_local run_script clean

all: build_image run_tests install_local run_script

build_image:
	docker build -t $(DOCKER_IMAGE_NAME) .

run_tests:
	$(PYTHON) -m unittest discover -s tests

install_local:
	$(PIP) install .

run_script:
	$(PYTHON) -m $(PACKAGE_NAME) --help

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf build dist *.egg-info

help:
	@echo "Makefile targets:"
	@echo "  all           - Build the Docker image, run tests, install package locally, and run the script"
	@echo "  build_image   - Build the Docker image from the Dockerfile"
	@echo "  run_tests     - Run the unit tests"
	@echo "  install_local - Install the package locally using pip"
	@echo "  run_script    - Run the Python script locally"
	@echo "  clean         - Remove temporary files and directories"
	@echo "  help          - Show this help message"
