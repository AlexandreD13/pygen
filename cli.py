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

    parser.add_argument("project_name", type=str, nargs=1,
                        help="The name of the project to create")

    parser.add_argument("-a", "--author", required=False, type=str, nargs=1,
                        default=["Anonymous"], help="Author name")

    parser.add_argument("-d", "--doc", action="store_false",
                        help="Deactivate documentation")

    parser.add_argument("-l", "--license", required=False, type=str, nargs=1,
                        default=["mit"], help="Generate specified LICENSE [\"mit\" (default), \"apache\", \"gnu3\"]")

    parser.add_argument("-v", "--verbose", action="store_true",
                        help="More information displayed")

    args = parser.parse_args(argv)
    project_directory = os.getcwd()

    print()
    generate_folders.create_folders(args, project_directory)
    generate_files.create_files(args, project_directory)
    print(f"{Color.BLUE}[  INFO  ] Files have been created successfully.{Color.END}")
