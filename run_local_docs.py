"""
Colvert - The Detection Use Case Management Tool
Copyright (C) 2025  The Colvert Contributors (see README.md / colvert/settings.py)

Licensed under the EUPL, Version 1.2 only (the "Licence");
You may not use this work except in compliance with the Licence.
You may obtain a copy of the Licence, available in the 23 official
languages of the European Union, at:
https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12
"""

import os
import sys
import argparse
import importlib
import subprocess
import socketserver
import http.server

def build_docs():
    """Install, import and run 'sphinx' to locally build the documentation.

    :raises FileNotFoundError: When docs source directory not found.
    """
    # ==> Dynamically loaded: from sphinx.application import Sphinx
    sphinx_package_name = 'sphinx'
    sphinx_module_name = 'application'
    sphinx_func_name = 'Sphinx'
    try:
        importlib.import_module(f".{sphinx_module_name}", sphinx_package_name)
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'sphinx'])
        print(f"[{__file__}] Installed sphinx package.")
    finally:
        globals()['sa'] = importlib.import_module(f".{sphinx_module_name}", sphinx_package_name)

    # ==> Run Sphinx
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DOCS_DIR = os.path.join(BASE_DIR, 'docs')

    if not os.path.exists(DOCS_DIR):
        raise FileNotFoundError(f"Docs source directory not found: {DOCS_DIR}")

    # Install Sphinx docs requirements
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', os.path.join(DOCS_DIR, 'requirements.txt')])

    sphinx_func = getattr(globals()['sa'], sphinx_func_name)
    if sphinx_func:
        app = sphinx_func(
            srcdir=DOCS_DIR,
            confdir=DOCS_DIR,
            outdir=os.path.join(DOCS_DIR, '_build'),
            doctreedir=os.path.join(DOCS_DIR, '_build', 'doctrees'),
            buildername='html'
        )
        app.build()

    # ==> Clean up
    del globals()['sa']

    index_gen_file = os.path.join(DOCS_DIR, 'index.rst') # Clean up index.rst generated from Jinja2 template
    if os.path.exists(index_gen_file):
        os.remove(index_gen_file)

    # We do not clean:
    # - Module sphinx installed above
    # - Sphinx requirements.txt installed modules

def run_server(ip: str = '127.0.0.1', port: int = 8888):
    """Run a local HTTP server to serve Sphinx docs.

    :param ip: Listening IP address (default: 127.0.0.1).
    :type ip: str
    :param port: Listening port (default: 8888).
    :type port: int
    """
    os.chdir('docs/_build')  # Sphinx docs build directory
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer((ip, port), handler) as httpd:
        print(f"Serving local docs at http://{ip}:{port}/")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping server...")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a local HTTP server to serve local Sphinx docs.")
    parser.add_argument('-i', '--ip', type=str, default='127.0.0.1', help='Listening IP address (default: 127.0.0.1)')
    parser.add_argument('-p', '--port', type=int, default=8888, help='Listening port (default: 8888)')
    parser.add_argument('-b', '--build', action='store_true', help='Build Sphinx docs before running the server')
    args = parser.parse_args()

    if args.build:
        build_docs()

    run_server(args.ip, args.port)
