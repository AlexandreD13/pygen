"""
Author:         Alexandre Desfosses
Creation date:  2023-03-11
Documentation:
References:
"""

from pygen.generate_files import create_file
from pygen.generate_folders import create_folder

import cli
import pytest
import os
import shutil

author: str = "Alexandre Desfosses"

project_name: str = "temp-project"

project_content: list[str] = [
    f"{project_name}",
    f"{project_name}\\docs\\",
    f"{project_name}\\docs\\.nojekyll",
    f"{project_name}\\doc-source\\",
    f"{project_name}\\doc-source\\_static\\",
    f"{project_name}\\doc-source\\_static\\fixed-theme-width.css",
    f"{project_name}\\doc-source\\_template\\",
    f"{project_name}\\doc-source\\getting-started\\",
    f"{project_name}\\doc-source\\getting-started\\getting-started.rst",
    f"{project_name}\\doc-source\\getting-started\\index.rst",
    f"{project_name}\\doc-source\\guides\\",
    f"{project_name}\\doc-source\\guides\\index.rst",
    f"{project_name}\\doc-source\\guides\\reStructuredText\\",
    f"{project_name}\\doc-source\\guides\\reStructuredText\\index.rst",
    f"{project_name}\\doc-source\\guides\\reStructuredText\\reStructuredText.rst",
    f"{project_name}\\doc-source\\guides\\sphinx\\",
    f"{project_name}\\doc-source\\guides\\sphinx\\index.rst",
    f"{project_name}\\doc-source\\guides\\sphinx\\sphinx.rst",
    f"{project_name}\\doc-source\\images\\",
    f"{project_name}\\doc-source\\conf.py",
    f"{project_name}\\doc-source\\index.rst",
    f"{project_name}\\{project_name}\\tests",
    f"{project_name}\\{project_name}\\__init__.py",
    f"{project_name}\\{project_name}\\__main__.py",
    f"{project_name}\\{project_name}\\helpers.py",
    f"{project_name}\\{project_name}\\tests\\__init__.py",
    f"{project_name}\\{project_name}\\tests\\{project_name}_tests.py",
    f"{project_name}\\setup.py",
    f"{project_name}\\LICENSE",
    f"{project_name}\\README.md",
    f"{project_name}\\.gitignore",
    f"{project_name}\\TODO.md",
    f"{project_name}\\requirements.txt",
    f"{project_name}\\Makefile",
    f"{project_name}\\make.bat",
    f"{project_name}\\cli.py",
]


@pytest.fixture
def cli_valid_arguments():
    """
    Description...

    :return:
    """

    return [
        project_name,
    ]


@pytest.fixture
def cli_invalid_arguments():
    """
    Description...

    :return:
    """

    return []


@pytest.fixture
def licenses_arguments():
    """
    Description...

    :return:
    """

    return [[project_name, "-a", author, "-l", "mit"],
            [project_name, "-a", author, "-l", "apache"],
            [project_name, "-a", author, "-l", "gnu3"]]


@pytest.fixture
def python_version_arguments():
    """
    Description...

    :return:
    """

    return [
        project_name,
        "-a", author,
    ]


class TestCli:
    """
    Important: Tests do not validate contents of files.

    """

    def test_valid_arguments(self, cli_valid_arguments):
        """
        Description...

        :param cli_valid_arguments: Valid arguments to create a new project.
        :return:
        """

        # Use CLI to create new project
        cli.cli(cli_valid_arguments)

        # Ensure all folders and files are created properly
        for path in project_content:
            assert os.path.exists(path) is True

        # Destroy created project
        shutil.rmtree(cli_valid_arguments[0])
        assert os.path.exists(cli_valid_arguments[0]) is False

    def test_invalid_arguments(self, cli_invalid_arguments):
        """
        Description...

        :param cli_invalid_arguments: Valid arguments to create a new project.
        :return:
        """

        try:
            # Use CLI to create new project
            cli.cli(cli_invalid_arguments)

        except SystemExit:
            assert True

    def test_project_already_exists(self, cli_valid_arguments):
        """
        Description...

        :param cli_valid_arguments: Valid arguments to create a new project.
        :return:
        """

        # Use CLI to create new project except directory already exists
        try:
            os.mkdir(cli_valid_arguments[0])
            cli.cli(cli_valid_arguments)

        except FileExistsError:
            assert True

        # Destroy created directory
        os.rmdir(cli_valid_arguments[0])

    def test_licenses(self, licenses_arguments):
        """
        Description...

        :param licenses_arguments: Valid arguments to create a new project with all possible licenses.
        :return:
        """

        for arguments in licenses_arguments:
            # Use CLI to create new project
            cli.cli(arguments)
            assert os.path.exists(arguments[0]) is True

            file = open(arguments[0] + "\\LICENSE").readline()
            template = open(f"pygen\\templates\\license-{arguments[-1]}.txt").readline()
            assert file == template

            # Destroy created project
            shutil.rmtree(arguments[0])
            assert os.path.exists(arguments[0]) is False


class TestFileCreation:
    """
    Important: Tests do not validate contents of files.

    """

    def test_valid_template(self, cli_valid_arguments):
        """
        Description...

        :param cli_valid_arguments: Valid arguments to create a new project.
        :return:
        """

        # Use CLI to create new project
        cli.cli(cli_valid_arguments)

        file = "temp-file.txt"

        # Create temp_file.txt with empty template
        create_file((author, project_name, False), file, "templates\\empty.txt")
        assert os.path.exists(file) is True

        # Destroy created project
        shutil.rmtree(cli_valid_arguments[0])
        assert os.path.exists(cli_valid_arguments[0]) is False

        # Delete the file
        os.remove(file)
        assert os.path.exists(file) is False

    def test_invalid_template(self, cli_valid_arguments):
        """
        Description...

        :param cli_valid_arguments: Valid arguments to create a new project.
        :return:
        """

        try:
            # Use CLI to create new project
            cli.cli(cli_valid_arguments)

            # Create temp_file.txt with template that does not exist
            create_file((author, project_name, False),
                        "temp-file.txt",
                        "templates\\template-that-does-not-exist.txt")

        except FileNotFoundError:
            assert True

            # Destroy created project
            shutil.rmtree(cli_valid_arguments[0])
            assert os.path.exists(cli_valid_arguments[0]) is False


class TestFolderCreation:
    """
    Description...

    """

    def test_valid_path(self):
        """
        Description...

        :return:
        """

        # Data
        folder = "temp-folder"

        # Create temp_folder/
        create_folder(folder)
        assert os.path.exists(folder) is True

        # Delete the file
        os.rmdir(folder)
        assert os.path.exists(folder) is False

    def test_invalid_path(self):
        """
        Description...

        :return:
        """

        try:
            # Create temp_folder/
            create_folder("\\missing-folder\\temp-folder")

        except FileNotFoundError:
            assert True
