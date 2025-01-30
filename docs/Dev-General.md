# General

This part contains information intended to help developers to understand the inner workings of Colvert and connectors.

This **Developer Documentation** may be refered as **"CodeDoc"**.

## Development Environment

### GitHub Codespaces Setup

Create a personal **GitHub Codespaces** from scratch with ```colvert-project/colvert``` and ```origin/main``` remote repository.

Some Visual Studio Code extensions can be settled in addition of default ones:

* Python (_Microsoft_)
* Python Debugger (_Microsoft_)
* Pylance (_Microsoft_)
* GitHub Actions (_GitHub_)
* GitHub Copilot (_GitHub_)
* GitHub Copilot Chat (_GitHub_)
* markdownlint (_David Anson_)
* Docker (_Microsoft_)
* DevDb (_Damilola Olowookere_)
  * `.devdbrc` (Also ignored in `.gitignore`)

```json
[
    {
        "type": "sqlite",
        "path": "/workspaces/colvert/db.sqlite3"
    }
]
```

* autoDocstring - Python Docstring Generator (_Nils Werner_)
  * <https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html>
  * Settings > Extensions > Python Docstring Generator configuration > _Docstring Format_ > `sphinx`

As reminder, in **GitHub Codespaces** states concerning opened tabs and settings (like color theme, etc.) are not saved until you set _Backup and Sync Settings_.

The usage of **GitHub Codespaces** is limited to **<u>your subscribed GitHub plan</u>**.

## Documentation Build

|File                   |Usage                                                                                                                    |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------|
|`static/`              |Classic favicon, logo, and other static file to serve.                                                                   |
|`docs/requirements.txt`|pip packages needed by Sphinx to build documentation. Commented.                                                         |
|`docs/conf.py`         |Sphinx configuration. Commented.                                                                                         |
|`CNAME`                |Define the base URL for documentation. Not used by GitHub as built using a workflow, but used by `conf.py`.              |
|`index.rst.j2`         |Jinja2 parsed first template (`conf.py`) to load docs from connectors, then Sphinx index using _reStructuredText_ format.|
|`[*/]*.md`             |All others documentation files in Markdown format.                                                                       |

Help links:

* Sphinx docs for `conf.py`: <https://www.sphinx-doc.org/en/master/usage/configuration.html>
* As we use `sphinx_rtd_theme` for Sphinx, here is some help for **docstrings** writing: <https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html>

.. attention::

TODO Be sure to write doctsrings using Sphinx format.

### Local Build

#### Running the Script

To run the script with default values:

```shell
python run_local_docs.py
```

To specify a custom IP address and port:

```shell
python run_local_docs.py -i 127.0.0.1 -p 8000
```

To build the documentation before running the server:

```shell
python run_local_docs.py -b
```

To display the help message:

```shell
python run_local_docs.py -h
```

This script will start a local HTTP server that serves the `index.html` file from the `_build` directory, allowing you to test the generated Sphinx documentation. If the `-b` or `--build` option is specified, it will build the documentation before starting the server.

**_Warning_**: Check script logs for warnings or errors afterwards.

### GitHub Pages Build

This process build and publish docs on [docs.colvert.io](https://docs.colvert.io).

It uses **Sphinx** with a third-party GitHub workflow in `.github/workflows/build-docs.yml` to trigger build on `git push` action. It uses the third-party action [`sphinx-notes/pages@v3`](https://github.com/sphinx-notes/pages).
