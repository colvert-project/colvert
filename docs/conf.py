"""
Colvert - The Detection Use Case Management Tool
Copyright (C) 2024  The Colvert Contributors (see README.md / colvert/settings.py)

Licensed under the EUPL, Version 1.2 only (the "Licence");
You may not use this work except in compliance with the Licence.
You may obtain a copy of the Licence, available in the 23 official
languages of the European Union, at:
https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

Configuration file for the Colvert documentation builder.

This file only contains a selection of the most common and needed options.
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Colvert'
author = 'The Colvert Contributors'
copyright = '2024-%Y, ' + author
version = '0.1' #TODO - Get from ?
release = '0.1.0' #TODO - Get from ?


# -- General configuration ---------------------------------------------------

extensions = [
    'myst_parser',
    'sphinx.ext.githubpages',
]

# Format of the date
today = '%d %B %Y'

numfig = True

#language = 'en'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

html_theme = 'sphinx_rtd_theme'
html_title = 'Colvert Documentation'
html_baseurl = 'docs.colvert.io' #TODO - Get from CNAME
# Copy of colvert_square_192px.png
html_logo = 'static/logo.png'
# Copy of colvert_square_16px.png
html_favicon = 'static/favicon.png'
#html_output_encoding = 'utf-8'
html_static_path = ['static']
html_show_sourcelink = False