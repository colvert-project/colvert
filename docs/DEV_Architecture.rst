#####################
Software Architecture
#####################

.. warning::
    *This document is a work in progress.*

**Colvert** is a web application written in **Python 3**, built on **Django 5** web framework with **AdminLTE 4** templates library for view and control parts, itself based on **Bootstrap 5**.

The architecture consists of:

* The main application.
* Connectors to get data from providers and contextual more-valued information.

.. contents::

**TODO** EXPLAIN CODE TREE / WEB APP TREE & ROUTES

Packages & Libraries
********************

.. table:: Packages & Libraries

    +---------------------------+--------+-------------+-----------------------------------------------------------------+
    |Library                    |Type    |Version      |Purpose & Documentation                                          |
    +===========================+========+=============+=================================================================+
    || **python**               || Engine|| >= 3.12    || Language in which Colvert is written with.                     |
    ||                          ||       ||            ||                                                                |
    ||                          ||       ||            || https://docs.python.org/3                                      |
    +---------------------------+--------+-------------+-----------------------------------------------------------------+
    || **django**               || pip   || 5.1.5      || Web Application Framework with standard web application        |
    ||                          ||       ||            || features, authentication, templating, ORM, etc.).              |
    ||                          ||       ||            ||                                                                |
    ||                          ||       ||            || https://docs.djangoproject.com/                                |
    +---------------------------+--------+-------------+-----------------------------------------------------------------+
    || whitenoise               || pip   || 6.7.0      || Django app to properly serve static files in production.       |
    ||                          ||       ||            ||                                                                |
    ||                          ||       ||            || https://whitenoise.readthedocs.io/                             |
    ||                          ||       ||            || https://github.com/evansd/whitenoise                           |
    +---------------------------+--------+-------------+-----------------------------------------------------------------+
    || django-mssql-backend     || pip   || 2.8.1      || Django app used for Microsoft SQL Server backend.              |
    || *pyodbc*                 ||       || -          || *Installed with django-mssql-backend.*                         |
    ||                          ||       ||            ||                                                                |
    ||                          ||       ||            || https://pypi.org/project/django-mssql-backend                  |
    ||                          ||       ||            || https://github.com/ESSolutions/django-mssql-backend            |
    +---------------------------+--------+-------------+-----------------------------------------------------------------+
    || djangorestframework      || pip   || 3.15.2     || Django app used for Colvert's backend API.                     |
    ||                          ||       ||            ||                                                                |
    ||                          ||       ||            || https://www.django-rest-framework.org/                         |
    ||                          ||       ||            || https://pypi.org/project/djangorestframework                   |
    ||                          ||       ||            || https://github.com/encode/django-rest-framework                |
    +---------------------------+--------+-------------+-----------------------------------------------------------------+
    || admin-lte                || npm   || 4.0.0-beta3|| Front-end templates used within Colvert's HTML templates.      |
    ||                          ||       ||            || *AdminLTE 4 templates are based on Bootsrap 5 (and*            |
    ||                          ||       ||            || *OverlayScrollbars plugin.*                                    |
    ||                          ||       ||            ||                                                                |
    ||                          ||       ||            || https://adminlte.io/                                           |
    ||                          ||       ||            || https://github.com/ColorlibHQ/AdminLTE                         |
    ||                          ||       ||            || https://www.npmjs.com/package/admin-lte                        |
    +---------------------------+--------+-------------+-----------------------------------------------------------------+
    || bootstrap                || npm   || ~5.3.3     || Web Front-End Framework (JavaScript & CSS).                    |
    || *@popperjs*              ||       || -          || *Popper.js is bundled with Bootstrap.*                         |
    ||                          ||       ||            ||                                                                |
    ||                          ||       ||            || https://getbootstrap.com/docs/5.3/getting-started/introduction |
    ||                          ||       ||            || https://getbootstrap.com/docs/5.3/getting-started/download     |
    +---------------------------+--------+-------------+-----------------------------------------------------------------+
    || bootstrap-icons          || npm   || ^1.11.3    || Icons font used in front-end web pages.                        |
    ||                          ||       ||            ||                                                                |
    ||                          ||       ||            || https://icons.getbootstrap.com/                                |
    +---------------------------+--------+-------------+-----------------------------------------------------------------+
    || overlayscrollbars        || npm   || ^2.10.1    || Scrollbar plugin that hides the native scrollbars and          |
    ||                          ||       ||            || provides custom styleable overlay scrollbars.                  |
    ||                          ||       ||            ||                                                                |
    ||                          ||       ||            || https://kingsora.github.io/OverlayScrollbars                   |
    ||                          ||       ||            || https://www.npmjs.com/package/overlayscrollbars                |
    +---------------------------+--------+-------------+-----------------------------------------------------------------+
    || @fontsource/source-sans-3|| npm   || ^5.1.1     || Font used in front-end web pages.                              |
    ||                          ||       ||            ||                                                                |
    ||                          ||       ||            || https://fontsource.org/fonts/source-sans-3                     |
    ||                          ||       ||            || https://www.npmjs.com/package/@fontsource/source-sans-3        |
    +---------------------------+--------+-------------+-----------------------------------------------------------------+

* The minimal required version of **Python** is set in ``APP_MINIMAL_PYTHON_VER`` in ``colvert/settings.py``.
* **Python Package** (*pip*) versions are set in ``requirements.txt``.
* **JS(+CSS) Library** (*npm*) versions are set in ``package.json``.

Dependencies Matrix
===================

* **TODO** Check with GitHub Dependabot?

Project Setup
*************

* **Python Package** versions are set in ``requirements.txt`` and  maintained with ``pip`` using.

* **JS+CSS Library** are pulled in using ``npm``, then copied within Colvert to be embedded offline as static libraries.

Upgrading tools can be done with:

.. code-block:: shell

    python -m pip install --upgrade pip
    npm install -g npm

.. note::
    Version can be checked with the following commands:

    .. code-block:: shell

        /workspaces/colvert (main) $ python --version
        Python 3.12.1
        /workspaces/colvert (main) $ python -m pip --version
        /workspaces/colvert (main) $ npm --version

Libraries Integration
=====================

Python packages management with ``pip``
---------------------------------------

* For the first installation:

.. code-block:: shell

    /workspaces/colvert (main) $ python -m pip -r requirements.txt

* For updates:

.. code-block:: shell

    /workspaces/colvert (main) $ python -m pip install --upgrade -r requirements.txt

JS+CSS libraries copy using ``npm``
-----------------------------------

.. code-block:: shell

    /workspaces/colvert (main) $ python manage.py buildcolvert -b

Then, update Django project's static files to take new files into account:

.. code-block:: shell

    /workspaces/colvert (main) $ python manage.py collectstatic

For future library update, run again commands above by replacing the Bootstrap / AdminLTE version to download. Update this documentation page accordingly.

**TODO**
<https://whitenoise.readthedocs.io/en/latest/index.html#quickstart-for-django-apps>  
<https://whitenoise.readthedocs.io/en/latest/django.html>

Annex - Django Project Initialization
*************************************

After *Python* packages have been installed and before integrating JS+CSS libraries, the Django project has been initialized a first time with the following commands:

.. code-block:: shell

    /workspaces/colvert (main) $ django-admin startproject colvert .
    /workspaces/colvert (main) $ python manage.py startapp core
    /workspaces/colvert (main) $ python manage.py startapp help
    /workspaces/colvert (main) $ python manage.py startapp api

**TODO**
Hint: <https://automationpanda.com/2018/02/06/starting-a-django-project-in-an-existing-directory/>
