Introduction
************

Documentation:

- https://docutils.sourceforge.io/docs/user/rst/quickref.html#footnotes
- https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

Admonitions
***********

Attention
+++++++++

.. code-block:: reStructuredText
    :linenos:

    .. attention::
        ATTENTION

**Example:**

.. attention::
    ATTENTION

Caution
+++++++

.. code-block:: reStructuredText
    :linenos:

    .. caution::
        CAUTION

**Example:**

.. caution::
    CAUTION

Danger
++++++

.. code-block:: reStructuredText
    :linenos:

    .. danger::
        DANGER

**Example:**

.. danger::
    DANGER

Deprecated
++++++++++

.. code-block:: reStructuredText
    :linenos:

    .. deprecated::
        vX.X.X Deprecation message.

**Example:**

.. deprecated::
    vX.X.X Deprecation message.

Error
+++++

.. code-block:: reStructuredText
    :linenos:

    .. error::
        ERROR

**Example:**

.. error::
    ERROR

Hint
++++

.. code-block:: reStructuredText
    :linenos:

    .. hint::
        HINT

**Example:**

.. hint::
    HINT

Important
+++++++++

.. code-block:: reStructuredText
    :linenos:

    .. important::
        IMPORTANT

**Example:**

.. important::
    IMPORTANT

Note
++++

.. code-block:: reStructuredText
    :linenos:

    .. note::
        NOTE

**Example:**

.. note::
    NOTE

See also
++++++++

.. code-block:: reStructuredText
    :linenos:

    .. seealso::
        SEE ALSO

**Example:**

.. seealso::
    SEE ALSO

Tip
+++

.. code-block:: reStructuredText
    :linenos:

    .. tip::
        TIP

**Example:**

.. tip::
    TIP

Warning
+++++++

.. code-block:: reStructuredText
    :linenos:

    .. warning::
        WARNING

**Example:**

.. warning::
    WARNING

Version added
+++++++++++++

.. code-block:: reStructuredText
    :linenos:

    .. versionadded::
        vX.X.X Version added message.

**Example:**

.. versionadded::
    vX.X.X Version added message.

Version changed
***************

.. code-block:: reStructuredText
    :linenos:

    .. versionchanged::
        vX.X.X Version changed message.

**Example:**

.. versionchanged::
    vX.X.X Version changed message.

Code blocks
+++++++++++

.. code-block:: reStructuredText
    :linenos:

    .. code-block:: python
        :linenos:

        your code here

**Example:**

.. code-block:: reStructuredText
    :linenos:

    your code here

Headings
++++++++

..  code-block:: reStructuredText
    :linenos:

    Heading 1.1
    ===========

    Heading 2.1
    -----------

    Heading 3.1
    ***********

    Heading 3.2
    ***********

    Heading 4.1
    +++++++++++

    Heading 1.2
    ===========

    Heading 2.2
    -----------

Images
++++++

.. code-block:: reStructuredText
    :linenos:

    .. image:: path/filename.png
        :height: 400
        :align: center
        :alt: Alternative text

Italic, bold and code text
++++++++++++++++++++++++++++

.. code-block:: reStructuredText
    :linenos:

    *Italic text*
    **Bold text**
    ``Inline text``

**Example:**

    *Italic text*
    **Bold text**
    ``Inline text``

Line separators
+++++++++++++++

..  code-block:: reStructuredText
    :linenos:

    ----------

**Example:**

----------

Links
+++++

Internal Pages (Custom anchor)
******************************

When you have two sections with the same title in a project, you will get build errors when
you have a link to either section, because Sphinx does not know which section to link to.

..  code-block:: reStructuredText
    :linenos:

    .. _RST Overview:

    Overview
    **********

    RST Overview content

    .. _Sphinx Overview:

    Overview
    *********

    Sphinx Overview content

In a ``:ref:`` command, you then use the anchor text.

..  code-block:: reStructuredText
    :linenos:

    This is a link to the RST Overview: :ref:`RST Overview`

    This is a link to the Sphinx Overview: :ref:`Sphinx Overview`

External Pages
**************

.. code-block:: reStructuredText
    :linenos:

    `Link text <link URL>`__

**Example:**

`Google <http://google.com>`__

Lists
++++++++++++

Bullet lists
************

.. code-block:: reStructuredText
    :linenos:

    - Object 1
    - Object 2
    - Object 3

**Example:**

- Object 1
- Object 2
- Object 3

Definition lists
****************

.. code-block:: reStructuredText
    :linenos:

    Object 1:
        This is the definition for Object 1.
    Object 2:
        This is the definition for Object 2.
    Object 3:
        This is the definition for Object 3.

**Example:**

Object 1:
    This is the definition for Object 1.
Object 2:
    This is the definition for Object 2.
Object 3:
    This is the definition for Object 3.

Enumerated lists
****************

.. code-block:: reStructuredText
    :linenos:

    1. Object 1
    2. Object 2
    3. Object 3

**Example:**

1. Object 1
2. Object 2
3. Object 3

Options lists
*************

.. code-block:: reStructuredText
    :linenos:

    -a            command-line option "a"
    -b file       options can have arguments
                  and long descriptions
    --long        options can be long also
    --input=file  long options can also have
                  arguments
    /V            DOS/VMS-style options too

**Example:**

-a            command-line option "a"
-b file       options can have arguments
              and long descriptions
--long        options can be long also
--input=file  long options can also have
              arguments
/V            DOS/VMS-style options too

Making a Glossary
+++++++++++++++++

..  code-block:: reStructuredText
    :linenos:

    .. glossary::

        environment
            A structure where information about all documents under the root is
            saved, and used for cross-referencing.  The environment is pickled
            after the parsing stage, so that successive runs only need to read
            and parse new and changed documents.

        source directory
            The directory which, including its subdirectories, contains all
            source files for one Sphinx project.

**Example:**

.. glossary::

Environment
    A structure where information about all documents under the root is
    saved, and used for cross-referencing.  The environment is pickled
    after the parsing stage, so that successive runs only need to read
    and parse new and changed documents.

Source directory
    The directory which, including its subdirectories, contains all
    source files for one Sphinx project.

Making a Table
++++++++++++++

.. code-block:: reStructuredText
    :linenos:

    .. list-table:: Title
        :widths: auto
        :header-rows: 1

        * - Header 1
          - Header 2
          - Header 3
          - Header 4
        * - Row 1, column 1
          - Row 1, column 2
          - Row 1, column 3
          - Row 1, column 4
        * - Row 2, column 1
          - Row 2, column 2
          - Row 2, column 3
          - Row 1, column 4

**Example:**

.. list-table:: This is the title
    :widths: auto
    :header-rows: 1

    * - Header 1
      - Header 2
      - Header 3
      - Header 4
    * - Row 1, column 1
      - Row 1, column 2
      - Row 1, column 3
      - Row 1, column 4
    * - Row 2, column 1
      - Row 2, column 2
      - Row 2, column 3
      - Row 1, column 4