"""
Author:         Alexandre Desfosses
Creation date:  2023-02-23
Documentation:
References:
"""

from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.readlines()

setup(
    name="pygen",
    version="0.1.0",
    packages=find_packages(
        exclude=[
            "pygen.tests"
        ],
    ),
    install_requires=requirements,
    url="https://github.com/AlexandreD13/pygen",
    license="MIT",
    author="Alexandre Desfosses",
    author_email="",
    description="A Python scaffolding tool",
    python_requires="==3.9",
    py_modules=["cli"],
    entry_points={
        "console_scripts": [
            "pygen = cli:cli"
        ]
    },
    package_data={"": ["templates/*.txt"]},
)
