Installing Pygen
================

To use Pygen, you need to add it to your PATH. Go to the root of Pygen
(where **setup.py** is):

..  code-block:: bash
    :emphasize-lines: 9

    ../pygen/
        pygen-doc-source/...
        pygen-doc-build/...
        pygen/...
        .gitignore
        cli.py
        LICENSE
        make.bat
        Makefile
        README.md
        requirements.txt
        setup.py
        TODO.md

and run:

..  code-block:: bash

    $ python setup.py build

    $ python setup.py install