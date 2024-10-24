# General

This **Developer Documentation** can be refered as **"CodeDoc"**.

## Development Environment

### GitHub Codespaces

Create a personal **GitHub Codespaces** from scratch with ```colvert-project/colvert``` and ```origin/main``` remote repository.

Some Visual Studio Code extensions can be settled in addition:

* Python
* Python Debugger
* Pylance
* GitHub Actions

As reminder, in **GitHub Codespaces** states concerning opened tabs and settings (like color theme, etc.) are not saved until you set _Backup and Sync Settings_.

### Documentation Build

It uses **Sphinx** with a third-party GitHub workflow in `.github/workflows/build-docs.yml` to trigger build on `git push` action. It uses the third-party action [`sphinx-notes/pages@v3`](https://github.com/sphinx-notes/pages).

|File                   |Usage                                                                                                                    |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------|
|`static/`              |Classic favicon, logo, and other static file to serve.                                                                   |
|`docs/requirements.txt`|pip packages needed by Sphinx to build documentation. Commented.                                                         |
|`docs/conf.py`         |Sphinx configuration. Commented.                                                                                         |
|`CNAME`                |Define the base URL for documentation. Not used by GitHub as built using a workflow, but used by `conf.py`.              |
|`index.rst.j2`         |Jinja2 parsed first template (`conf.py`) to load docs from connectors, then Sphinx index using _reStructuredText_ format.|
|`*.md`                 |All others documentation files in Markdown format.                                                                       |

Help links:

* Sphinx docs for `conf.py`: <https://www.sphinx-doc.org/en/master/usage/configuration.html>

# Architecture

[![Python 3.12+](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white&labelColor=3776ab&color=ffd43b)](https://www.python.org)
[![Django 5.1](https://img.shields.io/badge/Django-5.1-white?logo=django&logoColor=white&labelColor=092e20)](https://www.djangoproject.com)
([![Bootstrap 5](https://img.shields.io/badge/Bootstrap-5.3-white?logo=bootstrap&logoColor=white&labelColor=7952b3)](getbootstrap.com))

AdminLTE

**Colvert** is a web application written in **_Python_ 3**, built on **_Django_ 5** web framework with **_AdminLTE 4_** as **_Bootstrap_ 5** template for view and control parts.

## Project Setup

### Packages Installation

```shell
/workspaces/colvert (main) $ python --version
Python 3.12.1
/workspaces/colvert (main) $ pip --version
pip 24.2 from /usr/local/python/3.12.1/lib/python3.12/site-packages/pip (python 3.12)
```

```shell
 /workspaces/colvert (main) $ python -m pip install Django
 ...
 Successfully installed Django-5.1.1 asgiref-3.8.1 sqlparse-0.5.1
 /workspaces/colvert (main) $ django-admin --version
 5.1.1
```

```shell
 /workspaces/colvert (main) $ python -m pip install WhiteNoise
 ...
 Successfully installed whitenoise-6.7.0
```

### Django Project Initialization

Within the root repository folder ```/workspaces/colvert```.

```shell
/workspaces/colvert (main) $ django-admin startproject colvert .
/workspaces/colvert (main) $ python manage.py startapp core
```

Hint: <https://automationpanda.com/2018/02/06/starting-a-django-project-in-an-existing-directory/>

## Additional Libraries Installation

```shell
/workspaces/colvert (main) $ npm --version
10.8.2
```

* **AdminLTE**, admin dashboard & control panel theme. Built on top of Bootstrap.

<https://adminlte.io/>

<https://adminlte.io/docs/>

Bootstrap and AdminLTE installed in minimal version:

```shell
/workspaces/colvert (main) $ cd /workspaces

/workspaces $ npm install admin-lte@^4.0.0-beta2
/workspaces $ cp node_modules/admin-lte/dist/css/adminlte.min.css colvert/core/static/css/adminlte.min.css
/workspaces $ cp node_modules/admin-lte/dist/js/adminlte.min.js colvert/core/static/js/adminlte.min.js

/workspaces $ cd colvert
```

For future library update, run again commands above by replacing the Bootstrap / AdminLTE version to download.

## Development

* `main` branch for now.

### Docstrings

**Docstrings** is done using _reStructuredText_ formatting.

### Packaging & Run

Update `requirements.txt`

```shell
python manage.py migrate
python manage.py runserver
```

TODO - Collect staticfiles

TODO - Merge migrations
