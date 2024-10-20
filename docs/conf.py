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

import os
import sys

colvert_docs_root_reldir = '.'
colvert_root_reldir ='..'
colvert_main_reldir ='../colvert'
colvert_core_reldir ='../core'

sys.path.insert(0,
                os.path.abspath(colvert_docs_root_reldir),
                os.path.abspath(colvert_main_reldir),
                os.path.abspath(colvert_core_reldir))

# Directory name in colvert which acts as connectors repository
COLVERT_CONNECTORS_REPO_NAME = 'connectors'
# Directory name in connector to pull documentation from
CONNECTOR_DOCS_DIR_NAME = 'docs'

# -- Prework run -------------------------------------------------------------

from shutil import copytree
from jinja2 import Environment, FileSystemLoader

# => sphinx-apidoc
#TODO sphinx-apidoc

# => Import documentation from connectors

colvert_docs_connectors_abspath = os.path.abspath(os.path.join(colvert_docs_root_reldir, COLVERT_CONNECTORS_REPO_NAME))
colvert_connectors_repo_abspath = os.path.abspath(os.path.join(colvert_root_reldir, COLVERT_CONNECTORS_REPO_NAME))

# List of copied files to add to index
connectors_docs_files = []

# Copy docs directory from connectors to docs/connectors/{connector_name}/
for f in os.scandir(colvert_connectors_repo_abspath):
    if not f.is_dir():
        continue

    connector_docs_dir = os.path.join(f.path, CONNECTOR_DOCS_DIR_NAME)
    if not os.path.isdir(connector_docs_dir):
        continue
    else:
        colvert_docs_connector_dir = os.path.join(colvert_docs_connectors_abspath, f.name)
        copied_path = copytree(connector_docs_dir, colvert_docs_connector_dir, dirs_exist_ok=True)
        #TODO Manage subdir which is not the case here
        for f in os.listdir(copied_path):
            if f.endswith('.md') or f.endswith('.rst'):
                connectors_docs_files.append(os.path.relpath(f, colvert_docs_root_reldir))

# Create index.rst from Jinja2 template
env = Environment(loader=FileSystemLoader(searchpath=str(colvert_docs_root_reldir)))
index_template = env.get_template('index.rst.j2')
index_content = index_template.render(plugin_docs=connectors_docs_files)

with open(os.path.join(colvert_docs_root_reldir, 'index.rst'), 'w') as f:
    f.write(index_content)

# -- Project information -----------------------------------------------------

# Get project, author, version and release from colvert's settings.py file

project = 'Colvert' #TODO - Get from APP_SHORT_NAME
author = 'The Colvert Contributors' #TODO - Get from APP_CONTRIBUTORS
copyright = 'TODO' #TODO - Get from '%s, %s. %s. %s. %s' % (APP_YEARS, author, APP_CREATED_BY, APP_SPONSORED_BY, APP_POWERED_BY)
version = '0.1' #TODO - Get from APP_VERSION
release = '0.1.0' #TODO - Get from APP_VERSION

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
# Get html_baseurl from the "file variable" CNAME
html_baseurl = 'docs.colvert.io' #TODO - Get from CNAME
# Copy of colvert_square_192px.png
html_logo = 'static/logo.png'
# Copy of colvert_square_16px.png
html_favicon = 'static/favicon.png'
#html_output_encoding = 'utf-8'
html_static_path = ['static']
html_show_sourcelink = False