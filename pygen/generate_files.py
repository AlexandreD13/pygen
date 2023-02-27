"""
Author:         Alexandre Desfosses
Creation date:  2023-02-23
Documentation:
References:
"""

from pygen.color import Color
from string import Template

import datetime
import pkg_resources


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
        (f"{root}/{project_name}/tests/__init__.py", "templates/empty.txt"),
        (f"{root}/{project_name}/tests/{project_name}_tests.py", "templates/empty.txt"),
        (f"{root}/setup.py", "templates/setup.txt"),
        (f"{root}/LICENSE", f"templates/license-{args.license[0].lower()}.txt"),
        (f"{root}/README.md", "templates/readme.txt"),
        (f"{root}/.gitignore", "templates/gitignore.txt"),
        (f"{root}/TODO.md", "templates/todo.txt"),
        (f"{root}/requirements.txt", "templates/empty.txt"),
    ]

    for file in files_to_create:
        create_file(args, path=file[0], template=file[1])


def create_file(args, path: str, template: str) -> None:
    """

    :param args:
    :param path:
    :param template:
    :return:
    """
    content = pkg_resources.resource_string(__name__, template)
    content_template: Template = Template(content.decode("utf8").replace("\r", ""))
    content_string: str = content_template.safe_substitute(author_name=args.author[0],
                                                           date=str(datetime.datetime.now().strftime("%y/%m/%d")),
                                                           project_name=args.project[0],
                                                           python_version=args.python_version[0])
    open(path, "a").write(content_string)

    if args.verbose:
        print(f"{Color.BLUE}create:  +++{Color.END} {path}")
