Development
===========
We'd love you to contribute to *IFDat-docs*!


.. contents::
   :local:
   :backlinks: none

Issues
------

Questions, feature requests and bug reports are all welcome as [discussions or issues](https://github.com/lerooze/ifdat-docs/issues/new/choose).


Pull Requests
-------------

It should be relatively simple to get started and create a Pull Request.


You'll need to have a version between **python 3.8 and 3.12** and **git** installed.

.. code-block:: bash

    # 1. clone your fork and cd into the repo directory
    git clone git@github.com:<your username>/ifdat-docs.git
    cd ifdat-docs

    # 2. Set up a virtualenv
    python -m venv env

    # 3. Activate virtualenv
    source env/bin/activate

    # 4. Inatall ifdat-docs
    pip install --editable .[docs]

    # 5. Checkout a new branch and cd into docs 
    git checkout -b my-new-feature-branch
    cd docs

    # 5a (optional). Copy static files and recreate csv table source 
    make copy

    # 6 Make your changes 

    # 7. Build docx documentation
    make docx

    # 8. Copy docx documentation to static
    make copy_docx

    # 9. Build html documentation
    makc html

    #... commit, push, and create your pull request
