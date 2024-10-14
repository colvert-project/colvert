# Colvert CodeDoc

## General

### GitHub Codespaces

Using **GitHub Codespaces** from scratch with ```colvert-project/colvert``` as ```origin/main``` remote repository. Some customization settled in addition in VS Code:
* Choose your preferred **color theme**;
* Install **Python** (by Microsoft) extension.

As reminder in **GitHub Codespaces**, saved states about:
* **color theme**;
* Opened tabs;
are not guaranteed.

No problem with files state.

## Setting Up Project

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

### Django Project Initialization

Within the root repository folder ```/workspaces/colvert```.

```shell
/workspaces/colvert (main) $ django-admin startproject colvert .
/workspaces/colvert (main) $ python manage.py startapp core
```
Hint: <https://automationpanda.com/2018/02/06/starting-a-django-project-in-an-existing-directory/>

### Installing & Updating Additional Libraries

```shell
/workspaces/colvert (main) $ npm --version
10.8.2
```

* **AdminLTE**, admin dashboard & control panel theme. Built on top of Bootstrap.

<https://adminlte.io/>

<https://adminlte.io/docs/>

Install Bootstrap and AdminLTE in minimal version:
```shell
$ cd /workspaces

$ npm install admin-lte@^4.0.0-beta2
$ cp node_modules/admin-lte/dist/css/adminlte.min.css colvert/core/static/css/adminlte.min.css
$ cp node_modules/admin-lte/dist/js/adminlte.min.js colvert/core/static/js/adminlte.min.js

$ cd colvert
```
For library update, run again commands above by replacing the Bootstrap / AdminLTE version to download.

## Development

* `master` branch for now.

## Package & Run

_TODO_ pip freeze > requirements.txt

```shell
python manage.py migrate
python manage.py runserver
```

## Git Useful Commands

* Push **main** to **origin**:
```shell
git push origin main
```

IMPORTANT: Commands below come back to a full state, so files are ** deleted** and also **uncommited changes on versioned filesare lost**!

* To remove the last commit from git ():
```shell
git reset --hard HEAD^
```
* To remove multiple commits from the top (e.g. top 3):
```shell
git reset --hard HEAD~3
```
