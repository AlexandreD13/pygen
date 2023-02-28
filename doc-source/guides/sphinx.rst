Introduction
************

The Sphinx documentation is written using the
`reStructuredText <https://docutils.sourceforge.io/docs/user/rst/quickref.html#footnotes>`__ *.rst* language (though it
can also be written with the `Markdown <https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet>`__ *.md*
language).

Getting started
***************

In the root of the project:

..  code-block:: bash
    :emphasize-lines: 2, 3

    ../pygen/
        docs/...
        doc-source/
        pygen/...
        .gitignore
        cli.py
        LICENSE
        README.md
        requirements.txt
        setup.py
        TODO.md

and run the following command:

..  code-block:: bash
    :linenos:

    $ sphinx-build doc-source/ docs/

or

..  code-block:: bash
    :linenos:

    $ sphinx-autobuild doc-source/ docs/

See Next section about ``sphinx-autobuild``.

.. important::
    *docs/* should be built with the previous command, otherwise Github Pages won't be able to read the files
    properly. A *.nojekyll* file should also be added in the *docs/* folder if it is not already present.

`Sphinx autobuild <https://github.com/executablebooks/sphinx-autobuild>`__
**************************************************************************

Leave the *docs/* folder, then run the documentation on a local server which listens to any changes to the doc
and updates them live.

..  code-block:: bash
    :linenos:

    $ cd ..

    $ sphinx-autobuild doc-source/ docs/

`Sphinx themes <https://sphinx-rtd-theme.readthedocs.io/en/stable/>`__
**********************************************************************

Switching themes
++++++++++++++++

To change the theme, simply change the value ``html_theme = "sphinx_rtd_theme"`` *in conf.py* to any other theme.
You must also include the theme in your *setup.py*/*requirements.txt* files.

Top themes
++++++++++

.. attention::
    Change links to actual images of the themes with links to repos/install procedure.

Book
    Can easily be converted to *.pdf* or *.rst*.

    https://sphinx-themes.org/sample-sites/sphinx-book-theme/
Furo
    Has light/dark mode.

    https://sphinx-themes.org/sample-sites/furo/#
Groundwork
    Dark mode.

    https://sphinx-themes.org/sample-sites/groundwork-sphinx-theme/
Karma
    https://sphinx-themes.org/sample-sites/karma-sphinx-theme/
Press
    https://sphinx-themes.org/sample-sites/sphinx-press-theme/
Read The Docs
    https://sphinx-themes.org/sample-sites/sphinx-rtd-theme/
Renku
    https://sphinx-themes.org/sample-sites/renku-sphinx-theme/