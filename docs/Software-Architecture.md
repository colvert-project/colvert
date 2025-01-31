# Software Architecture

**Colvert** is a web application written in **_Python_ 3**, built on **_Django_ 5** web framework with **_AdminLTE 4_** templates library for view and control parts, itself based on **_Bootstrap_ 5**.

The architecture consists of:

* The main application.
* Connectors to potentially get data from providers and contextual more-valued information.

## Packages & Libraries

|Library|Type|Version|Purpose|
|----------|------|------|-|
|_Python_      |Engine|3.12.1     |Language in which Colvert is written with|
|**Django**    |Python|5.1.5      |Web Application Framework (Basic application features, Templating, ORM)|
|**WhiteNoise**|Python|6.7.0      |Server properly static files in production **AND** in debug mode|
|AdminLTE      |CSS+JS|4.0.0-beta3|Front-end library used with HTML templates|
|Bootstrap     |CSS+JS|5.3.3      |Embedded within AdminLTE 4.0.0-beta3|

* Type means type of library.

* In `requirements.txt`, versions are fixed.
* In Python package, versions must be assume as 'at least', to let potential already deployed packages as is.

 [![AdminLTE 4.0](https://img.shields.io/npm/v/admin-lte/latest.svg)](https://www.npmjs.com/package/admin-lte)  

 ([![Bootstrap 5.3](https://img.shields.io/badge/Bootstrap-5.3-white?logo=bootstrap&logoColor=white&labelColor=7952b3)](getbootstrap.com))

### Dependencies Matrix

* _TODO_ Check with GitHub Dependabot

### Official Documentation

* Python

<https://docs.djangoproject.com/>

* WhiteNoise

* AdminLTE

 <https://adminlte.io>  

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

#### Python Libraries Upgrade

* pip

```shell
python -m pip install --upgrade pip
```

### Django Project Initialization

Within the root repository folder ```/workspaces/colvert```.

```shell
/workspaces/colvert (main) $ django-admin startproject colvert .
/workspaces/colvert (main) $ python manage.py startapp core
```

Hint: <https://automationpanda.com/2018/02/06/starting-a-django-project-in-an-existing-directory/>

### Additional Libraries Installation

```shell
/workspaces/colvert (main) $ npm --version
10.8.2
```

* **AdminLTE**, admin dashboard & control panel theme. Built on top of Bootstrap.

References:
<https://adminlte.io/>  
<https://adminlte.io/docs/>

Bootstrap and AdminLTE installed in minimal version:

```shell
/workspaces/colvert (main) $ cd /workspaces
/workspaces $ npm install admin-lte@^4.0.0-beta3
/workspaces $ cp node_modules/admin-lte/dist/css/adminlte.min.css colvert/core/static/css/adminlte.min.css
/workspaces $ cp node_modules/admin-lte/dist/js/adminlte.min.js colvert/core/static/js/adminlte.min.js
/workspaces $ npm rm admin-lte
/workspaces $ cd colvert
```

Then, update static files:

```shell
/workspaces/colvert (main) $ python manage.py collectstatic
```

For future library update, run again commands above by replacing the Bootstrap / AdminLTE version to download.

## Development

* `main` branch for now.

### Docstrings

**Docstrings** is done using _reStructuredText_ formatting.

### Model Management

#### Strategy

We avoid :

```shell
# Generate an empty migration file from the given app
python manage.py makemigrations --empty core --name add_defaults
```

TODO doc. signal

#### Reset migration files & DB

1. Delete `migrations/__pycache__`.
2. Delete problematic or all `migrations/<XXXX_MIG>.py` files.
3. Delete `db.sqlite3` file.
4. `python manage.py makemigrations` (create also empty db.sqlite3 if not existing).
5. `python manage.py migrate` to apply model in DB, will also set default values if they do not exist using the Django Signals approach.

#### Model Migration Cheatsheet

```shell
# Generate migration files from the given app, or for all apps if not given
python manage.py makemigrations [<APP>]

# TODO
python manage.py squashmigrations core 0001 0003

# To apply model in DB
python manage.py migrate

# TODO
python manage.py showmigrations
```

### Fixtures

TODO: python manage.py loaddata core/fixtures

#### Static Files Management

```shell
python manage.py collectstatic # To publish all static files in STATIC_ROOT if new ones need to
```

### Packaging & Run

1. Update `requirements.txt`
2. Migrate model if needed
3. Publish static files if needed
4. Run development server:

```shell
python manage.py runserver
```

#### References

<https://help.pythonanywhere.com/pages/DjangoStaticFiles/>  
<https://docs.djangoproject.com/en/dev/howto/static-files/>  
<https://docs.djangoproject.com/en/5.1/howto/static-files/deployment/>
