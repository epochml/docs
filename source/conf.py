# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
sys.path.insert(0, os.path.abspath("./_ext"))

# -- Project information -----------------------------------------------------

project = 'Epoch'
copyright = '2025, Epoch members'
author = 'Epoch members'

# The full version, including alpha/beta/rc tags
release = '1.0'
html_title = 'Epoch'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser', # Markdown support
    'sphinx_design', # Grids, cards, icons, etc.
    'sphinx_copybutton', # Copy button to the right of code blocks
    'makedomain', # Domain to document GNUstep Make
]
myst_enable_extensions = [
    'colon_fence'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'
# html_theme = 'pydata_sphinx_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_extra_path = ['RawHTML']

myst_footnote_transition = False

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css"
]
