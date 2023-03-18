"""
Author:         Alexandre Desfosses
Creation date:  2023-02-21
Documentation:
References:
"""

from pygen.color import Color
from textwrap import dedent

import os


def create_folders(args, project_directory: str) -> None:
    """
    Description...

    :param args: Arguments received by command-line interface (project, verbose).
    :param project_directory: Directory where files will be created.
    :return: None
    """

    project_name: str = args.project_name[0]

    root_directory: str = create_path(project_directory, project_name)
    if os.path.exists(root_directory) and os.listdir(root_directory):
        error_message: str = f"{Color.RED}[ FAILED ] {root_directory} already exists and is not empty. " \
                             f"Please try a different project name or root directory.{Color.END}"
        raise IOError(000, dedent(error_message))
    else:
        create_folder(root_directory, args.verbose)

    folders_to_create = [
        project_name,
        project_name + "\\tests",
    ]

    if args.doc:
        folders_to_create.extend([
            "docs\\",
            "doc-source\\",
            "doc-source\\_static\\",
            "doc-source\\_template\\",
            "doc-source\\getting-started\\",
            "doc-source\\guides\\",
            "doc-source\\guides\\reStructuredText\\",
            "doc-source\\guides\\sphinx\\",
            "doc-source\\images\\"
        ])

    for folder in folders_to_create:
        directory = create_path(root_directory, folder)
        create_folder(directory, args.verbose)


def create_folder(path: str, verbose: bool = False) -> None:
    """
    Description...

    :param path: Folder to create
    :param verbose: Verbose On/Off
    :return: None
    """

    os.mkdir(path)
    if os.path.exists(path) is False:
        error_message = f"{Color.RED}[ FAILED ] Unable to create root directory {path}. Path does not exist.{Color.END}"
        raise IOError(000, error_message, '')

    if verbose:
        print(f"{Color.BLUE}[  INFO  ]{Color.END} created at {os.path.abspath(path)}")


def create_path(project_directory: str, folder_name: str) -> str:
    """
    Description...

    :param project_directory: Directory where files will be created.
    :param folder_name: Name of the folder to create.
    :return: Path of the folder to create
    """

    project_directory: str = os.path.abspath(project_directory)
    return os.path.join(project_directory, folder_name)
