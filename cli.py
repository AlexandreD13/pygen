"""
Author:         Alexandre Desfosses
Creation date:  2023-02-23
Documentation:
References:
"""

from pygen import generate_files, generate_folders
from pygen.color import Color

import argparse
import os


def cli(argv=None):
    """
    Description...

    :param argv: Injected CLI arguments.
    :return: None
    """

    parser = argparse.ArgumentParser(prog="PyGen",
                                     description="A Python scaffolding tool")

    parser.add_argument("--project", required=True, type=str, nargs=1,
                        help="The name of the project to create")

    parser.add_argument("--path", required=False, type=str, nargs=1,
                        help="The path where the project will be initialized")

    parser.add_argument("--license", required=False, type=str, nargs=1,
                        default=["mit"], help="Generate specified LICENSE (default: \"mit\", \"apache\", \"gnu3\")")

    parser.add_argument("--verbose", action="store_true",
                        help="More information displayed")

    parser.add_argument("--author", required=True, type=str, nargs=1,
                        help="Author name")

    parser.add_argument("--python_version", required=False, type=str, nargs=1,
                        default="3.9", help="Specify the Python version to use")

    args = parser.parse_args(argv)
    project_directory = os.getcwd()

    if args.path is not None:
        project_directory = args.path[0]

    print()
    generate_folders.create_folders(args, project_directory)
    generate_files.create_files(args, project_directory)
    print(f"{Color.BLUE}[  INFO  ] Files have been created successfully.{Color.END}")
