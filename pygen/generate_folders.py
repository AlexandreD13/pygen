"""
Author:         Alexandre Desfosses
Creation date:  2023-02-21
Documentation:
References:
"""

from pygen.color import Color
from textwrap import dedent

import os


def create_folder(args, project_directory: str) -> None:
    """

    :param args:
    :param project_directory:
    :return:
    """
    project_name: str = args.project[0]
    root_directory: str = create_path(project_directory, project_name)
    if os.path.exists(root_directory) and os.listdir(root_directory):
        error_message: str = f"{Color.RED}{root_directory} already exists and is not empty. " \
                             f"Please try a different project name or root directory.{Color.END}"
        raise IOError(000, dedent(error_message))
    else:
        make_folder(root_directory, args.verbose)

    directory_names = [
        project_name,
        project_name + "/tests",
        project_name + "-doc-build",
        project_name + "-doc-source",
        project_name + "-doc-source/_static/",
        project_name + "-doc-source/_template/",
        project_name + "-doc-source/getting-started/",
        project_name + "-doc-source/guides/",
        project_name + "-doc-source/guides/reStructuredText/",
        project_name + "-doc-source/guides/sphinx/",
        project_name + "-doc-source/images/"
    ]

    for item in directory_names:
        directory = create_path(root_directory, item)
        make_folder(directory, args.verbose)


def make_folder(path: str, verbose: bool = False) -> None:
    """

    :param path:
    :param verbose:
    :return:
    """
    os.mkdir(path)
    if os.path.exists(path) is False:
        error_message = f"{Color.RED}Unable to create root directory {path}. Path does not exist.{Color.END}"
        raise IOError(000, error_message, '')

    if verbose:
        print(f"{Color.BLUE}[ INFO ]{Color.END} created at {os.path.abspath(path)}")


def create_path(project_directory: str, folder_name: str) -> str:
    """

    :param project_directory:
    :param folder_name:
    :return:
    """
    project_directory: str = os.path.abspath(project_directory)
    return os.path.join(project_directory, folder_name)
