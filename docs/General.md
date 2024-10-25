# General

This **Developer Documentation** may be refered as **"CodeDoc"**.

## Development Environment

### GitHub Codespaces

Create a personal **GitHub Codespaces** from scratch with ```colvert-project/colvert``` and ```origin/main``` remote repository.

Some Visual Studio Code extensions can be settled in addition of default ones:

* Python (_Microsoft_)
* Python Debugger (_Microsoft_)
* Pylance (_Microsoft_)
* GitHub Actions (_GitHub_)
* markdownlint (_David Anson_)
* Docker (_Microsoft_)

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
|`*.md`                 |All others documentation files in Markdown format.                                                                       |

Help links:

* Sphinx docs for `conf.py`: <https://www.sphinx-doc.org/en/master/usage/configuration.html>

# Architecture

**Colvert** is a web application written in **_Python_ 3**, built on **_Django_ 5** web framework with **_AdminLTE 4_** templates library for view and control parts, itself based on **_Bootstrap_ 5**.

## Packages & Libraries

|Library|Type|Version|Purpose|
|----------|------|------|-|
|_Python_      |Engine|3.12.1     |Language in which Colvert is written with|
|**Django**    |Python|5.1.1      |Web Application Framework (Basic application features, Templating, ORM)|
|**WhiteNoise**|Python|6.7.0      |Server properly static files in production **AND** in debug mode|
|AdminLTE      |CSS+JS|4.0.0-beta2|Front-end library used with HTML templates|
|Bootstrap     |CSS+JS|5().3?       ||

* Type means type of library.

* In `requirements.txt`, versions are fixed.
* In Python package, versions must be assume as 'at least', to let potential already deployed packages as is.

 [![AdminLTE 4.0](https://img.shields.io/npm/v/admin-lte/latest.svg)](https://www.npmjs.com/package/admin-lte)  
 _TODO_ Fix version, not latest  
 <https://adminlte.io>  
 ([![Bootstrap 5.3](https://img.shields.io/badge/Bootstrap-5.3-white?logo=bootstrap&logoColor=white&labelColor=7952b3)](getbootstrap.com))

### Dependencies Matrix

* _TODO_ Check with GitHub Dependabot

### Official Documentation

* Python

<https://docs.djangoproject.com/>

* WhiteNoise

AdminLTE

* Bootstrap

## Project Setup

### Libraries Installation

```shell
/workspaces/colvert (main) $ python --version
Python 3.12.1
/workspaces/colvert (main) $ pip --version
pip 24.2 from /usr/local/python/3.12.1/lib/python3.12/site-packages/pip (python 3.12)
```

```shell
/workspaces/colvert (main) $ python -m pip -r requirements.txt
```

<https://whitenoise.readthedocs.io/en/latest/index.html#quickstart-for-django-apps>  
<https://whitenoise.readthedocs.io/en/latest/django.html>

* Applying Quickstart (only for MIDDLEWARE), 1., 2. & 5.

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
python manage.py migrate # To update model if changed
python manage.py collectstatic # To publish all static files in STATIC_ROOT if new ones need to
python manage.py runserver # Start development server
```

TODO - Merge migrations

#### References

<https://help.pythonanywhere.com/pages/DjangoStaticFiles/>  
<https://docs.djangoproject.com/en/dev/howto/static-files/>  
<https://docs.djangoproject.com/en/5.1/howto/static-files/deployment/>
