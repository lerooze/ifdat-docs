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

It should be extremely simple to get started and create a Pull Request.


You'll need to have a version between **python 3.8 and 3.11** and **git** installed.

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

    # 5. Checkout a new branch and make your changes
    git checkout -b my-new-feature-branch
    # make your changes...

    # 6. Build documentation
    sphinx-build -b html docs/source docs/_build/html

    # ... commit, push, and create your pull request
