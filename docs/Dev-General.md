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
* SQLite Viewer (_Florian Klampfer_)
* autoDocstring - Python Docstring Generator (_Nils Werner_)
    + <https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html>
    + Settings > Extensions > Python Docstring Generator configuration > _Docstring Format_ > `sphinx`

As reminder, in **GitHub Codespaces** states concerning opened tabs and settings (like color theme, etc.) are not saved until you set _Backup and Sync Settings_.

## Documentation Build

It uses **Sphinx** with a third-party GitHub workflow in `.github/workflows/build-docs.yml` to trigger build on `git push` action. It uses the third-party action [`sphinx-notes/pages@v3`](https://github.com/sphinx-notes/pages).

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
