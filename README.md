# PyGen

### Build/Install
Go to the root of pygen and run:
````bash
> python setup.py build

> python setup.py install
````

You can then call PyGen from the command line anywhere to create a new Python project
basic folder hierarchy.

### setup.py example
- https://github.com/popojargo/orchester

### Pipx
- https://pypa.github.io/pipx/

### Generating the structure
- https://github.com/Aaronontheweb/scaffold-py/tree/master/scaffold

### Generating the venv
- https://stackoverflow.com/questions/57921255/how-to-create-python-virtual-environment-within-a-python-script#:~:text=To%20create%20a%20virtual%20env,a%20single%20line%20of%20code.&text=You%20can%20then%20activate%20this,custom%20packages%20using%20pip%20module
- https://docs.python.org/3/library/venv.html

### argparse
- https://docs.python.org/3/library/argparse.html

### Writing documentation
- https://www.sphinx-doc.org/en/master/usage/quickstart.html

Move to the *docs/* directory and run:
````bash
# where "builder" is one of the supported builders, e.g. html, pdf, epub, latex or linkcheck
>  make builder
````