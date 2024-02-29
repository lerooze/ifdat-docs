# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?= -w errors.txt
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = ifdat-docs
SOURCEDIR     = ./source
BUILDDIR      = _build/html
PYTHON        = python

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

copy:
	@$(PYTHON) copy.py

copy_docx:
	@$(PYTHON) copy_docx.py

.PHONY: help copy copy_docx Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
