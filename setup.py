"""
Author:         Alexandre Desfosses
Creation date:  2023-02-23
Documentation:
References:
"""

from setuptools import setup, find_packages

setup(
    name="pygen",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Sphinx~=6.1.3",
        "sphinx-autobuild~=2021.3.14",
        "furo~=2022.12.7"
    ],
    url="",
    license="",
    author="Alexandre Desfosses",
    author_email="",
    description="A Python scaffolding tool",
    python_requires="~=3.6",
    py_modules=["cli"],
    entry_points={
        "console_scripts": [
            "pygen = cli:parse_args"
        ]
    },
    include_package_data=True,
    package_data={"": ["templates/*.txt"]},
)
