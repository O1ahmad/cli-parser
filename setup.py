from setuptools import find_packages, setup

setup(
    name="cli_parser",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "cli_parser=src.parser:main",
        ],
    },
)
