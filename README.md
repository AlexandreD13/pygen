# PyGen

### Build / Install

Go to the root of pygen and run:
````bash
$ python setup.py build

$ python setup.py install
````

You can then call PyGen from the command line anywhere to create a new Python project
basic folder hierarchy.

### Install dependencies in venv

Make sure *venv* is activated, then run:
````bash
$ python setup.py build

$ python setup.py install
````

### Pytest

Pytest requirements: **Python 3.7+ or PyPy3**

Make sure *venv* is activated, then run:
````bash
$ pytest

# Quite useful
# -v = verbose
# -q = quiet
$ pytest --show-capture=no -v
````