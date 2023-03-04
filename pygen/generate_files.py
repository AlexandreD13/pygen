"""
Author:         Alexandre Desfosses
Creation date:  2023-02-23
Documentation:
References:
"""

from pygen.color import Color
from string import Template

import datetime
import glob
import os
import pkg_resources
import shutil


def create_files(args, project_directory: str) -> None:
    """

    :param args:
    :param project_directory:
    :return:
    """
    project_name: str = args.project[0]
    root: str = project_directory + "/" + project_name

    files_to_create: list[tuple] = [
        (f"{root}/{project_name}/__init__.py", "templates/empty.txt"),
        (f"{root}/{project_name}/__main__.py", "templates/empty.txt"),
        (f"{root}/{project_name}/helpers.py", "templates/empty.txt"),
        (f"{root}/{project_name}/tests/__init__.py", "templates/empty.txt"),
        (f"{root}/{project_name}/tests/{project_name}_tests.py", "templates/empty.txt"),
        (f"{root}/{project_name}-doc-source/getting-started/getting-started.rst", "templates/getting-started_getting-started.txt"),
        (f"{root}/{project_name}-doc-source/getting-started/index.rst", "templates/getting-started_index.txt"),
        (f"{root}/{project_name.capitalize()}-doc-source/guides/reStructuredText/index.rst", "templates/guides_reStructuredText_index.txt"),
        (f"{root}/{project_name.capitalize()}-doc-source/guides/reStructuredText/reStructuredText.rst", "templates/guides_reStructuredText_reStructuredText.txt"),
        (f"{root}/{project_name}-doc-source/guides/sphinx/index.rst", "templates/guides_sphinx_index.txt"),
        (f"{root}/{project_name}-doc-source/guides/sphinx/sphinx.rst", "templates/guides_sphinx_sphinx.txt"),
        (f"{root}/{project_name}-doc-source/guides/index.rst", "templates/guides_index.txt"),
        (f"{root}/{project_name}-doc-source/_static/fixed-theme-width.css", "templates/fixed-theme-width.txt"),
        (f"{root}/{project_name}-doc-source/conf.py", "templates/conf.txt"),
        (f"{root}/{project_name}-doc-source/index.rst", "templates/index.txt"),
        (f"{root}/setup.py", "templates/setup.txt"),
        (f"{root}/LICENSE", f"templates/license-{args.license[0].lower()}.txt"),
        (f"{root}/README.md", "templates/readme.txt"),
        (f"{root}/.gitignore", "templates/gitignore.txt"),
        (f"{root}/TODO.md", "templates/todo.txt"),
        (f"{root}/requirements.txt", "templates/empty.txt"),
        (f"{root}/Makefile", "templates/makefile.txt"),
        (f"{root}/make.bat", "templates/make.txt"),
        (f"{root}/cli.py", "templates/cli.txt"),
    ]

    try:
        for file in files_to_create:
            create_file(args, path=file[0], template=file[1])
    except OSError as error:
        raise Exception(f"\n{Color.RED}[FAILED] " + error.__str__() + f"{Color.END}")


def create_file(args, path: str, template: str) -> None:
    """

    :param args:
    :param path:
    :param template:
    :return:
    """
    project_name: str = args.project[0]
    project_name_cap = project_name.capitalize()

    content = pkg_resources.resource_string(__name__, template)
    content_template: Template = Template(content.decode("utf8").replace("\r", ""))
    content_string: str = content_template.safe_substitute(author_name=args.author[0],
                                                           date=str(datetime.datetime.now().strftime("%y/%m/%d")),
                                                           project_name=project_name,
                                                           project_name_cap=project_name_cap,
                                                           python_version=args.python_version[0])
    open(path, "a").write(content_string)

    if args.verbose:
        print(f"{Color.BLUE}[ INFO ]{Color.END} created at {path}")
