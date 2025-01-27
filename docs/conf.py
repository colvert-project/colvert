"""
Colvert - The Detection Use Case Management Tool
Copyright (C) 2024  The Colvert Contributors (see README.md / colvert/settings.py)

Licensed under the EUPL, Version 1.2 only (the "Licence");
You may not use this work except in compliance with the Licence.
You may obtain a copy of the Licence, available in the 23 official
languages of the European Union, at:
https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

Configuration file for Sphinx, the Colvert documentation builder.

This file only contains a selection of the most common and needed options.
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

# == Path setup ==============================================================

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys

COLVERT_DOCS_RELDIR = '.'
COLVERT_MAIN_APP_RELDIR ='../colvert'
COLVERT_CORE_APP_RELDIR ='../core'

sys.path.insert(0, os.path.abspath(COLVERT_DOCS_RELDIR))
sys.path.append(os.path.abspath(COLVERT_MAIN_APP_RELDIR))
sys.path.append(os.path.abspath(COLVERT_CORE_APP_RELDIR))

# == Prework run =============================================================

from shutil import copytree
from jinja2 import Environment, FileSystemLoader

# ==> sphinx-apidoc
# TODO: sphinx-apidoc

# ==> Import documentation from connectors

connectors_docs_files = [] # List of copied files to add to index

# Copy [ROOT]connectors/{found_connector}/docs directory to [ROOT]docs/connectors/{connector_name}/
for conn in os.scandir(os.path.abspath('../connectors')):
    if conn.is_dir():
        found_connector_docs = os.path.join(conn.path, 'docs')
        if os.path.isdir(found_connector_docs):
            copied_path = copytree(found_connector_docs, os.path.join(os.path.abspath(os.path.join(COLVERT_DOCS_RELDIR, 'connectors')), conn.name), dirs_exist_ok=True)
            # TODO: Manage subdir which is not the case here
            for f in os.listdir(copied_path):
                if f.endswith('.rst') or f.endswith('.md'):
                    connectors_docs_files.append(os.path.relpath(f, COLVERT_DOCS_RELDIR))

# Create index.rst from Jinja2 template
env = Environment(loader=FileSystemLoader(searchpath=str(COLVERT_DOCS_RELDIR)))
with open(os.path.join(COLVERT_DOCS_RELDIR, 'index.rst'), 'w') as f:
    f.write(env.get_template(os.path.join(COLVERT_DOCS_RELDIR, 'index.rst.j2')).render(connectors_docs_files=connectors_docs_files))

# == Get project information =================================================

# Get project, author, version and release from colvert/settings.py file
import settings # Because COLVERT_MAIN_APP_RELDIR has been aded into sys.path

project = settings.APP_SHORT_NAME
author = settings.APP_CONTRIBUTORS
copyright = '%s, %s. %s. %s. %s' % (settings.APP_YEARS, author, settings.APP_CREATED_BY, settings.APP_SPONSORED_BY, settings.APP_POWERED_BY)
version = '.'.join(settings.APP_VERSION.split('.')[:2])
release = settings.APP_VERSION

# == Sphinx configuration ====================================================

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
with open(os.path.join(COLVERT_DOCS_RELDIR, 'CNAME')) as f: # Get html_baseurl from the "file variable" CNAME
    html_baseurl = f.readline().strip('\n')
html_logo = 'static/logo.png' # Copy of colvert_square_192px.png
html_favicon = 'static/favicon.png' # Copy of colvert_square_16px.png
#html_output_encoding = 'utf-8'
html_static_path = ['static']
html_show_sourcelink = False
