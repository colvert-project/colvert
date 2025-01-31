########################
How to Configure Colvert
########################

If it doesn't already exist (as at the first run), Colvert will create ``colvert.yml`` configuration file with defaults settings.

You can modify the settings in ``colvert.yml`` to suit your requirements.

.. note::

    You can also reset the configuration to the default settings by deleting ``colvert.yml`` and restarting the application, or by copying ``colvert.template.yml`` to ``colvert.yml``.

File colvert.yml
================

Configuration
-------------

``colvert.yml`` is the configuration file for Colvert. It is located in the root directory of the application and must be set with the configuration settings below.

.. note::

    By default, Colvert uses the **SQLite** local database. You can change the database settings to use other databases such as **PostgreSQL**, **MySQL**, **Oracle** or **Microsoft SQL Server**.

* ``org-name: 'Colvert'`` Name of your organization.

    * *Type*: string
    * *Example*: ``'Colvert'``

* ``org-logo: 'org_180px.png'`` Path to your organization logo.

    * *Type*: string
    * *Example*: ``'org_180px.png'``

* ``debug: 'false'`` Enables or disables debug mode.

    * *Type*: string
    * *Values*: ``'true'`` or ``'false'``
    * *Default*: ``'false'``

* ``allowed-hosts:`` A list of strings representing the host/domain names that Colvert can serve.

    * *Type*: list of strings
    * *Example* and *Default*:

.. code-block:: yaml

    allowed-hosts:
      - 'yourdomain.com'
      - 'www.yourdomain.com'

.. end:: yaml

.. code-block:: yaml

    allowed-hosts:
      - '*'

.. end:: yaml

* ``csrf-trusted-origins:`` A list of trusted origins for CSRF protection.

    * *Type*: list of strings
    * *Example* and *Default*:

.. code-block:: yaml

    csrf-trusted-origins:
      - 'http://yourdomain.com'
      - 'https://yourdomain.com'
      - 'http://www.yourdomain.com'
      - 'https://www.yourdomain.com'

.. end:: yaml

.. code-block:: yaml

    csrf-trusted-origins:
      - 'http://'
      - 'https://'

.. end:: yaml

* ``database:`` Database configuration settings.

    * ``engine:`` The database backend to use.

        * *Type*: string
        * *Values*: ``'django.db.backends.sqlite3'`` or ``'django.db.backends.postgresql'`` or ``'django.db.backends.mysql'`` or ``'django.db.backends.oracle'`` or ``'sql_server.pyodbc'``
        * *Default*: ``'django.db.backends.sqlite3'``

    * ``host:`` The host of the database server, applicable for PostgreSQL, MySQL, Oracle and Microsoft SQL Server.

        * *Type*: string
        * *Example*: ``'dbserver.local'`` or ``'dbcluster\dbinstance'`` for MS SQL
        * *Default*: ``''``
        * *Note*: Not specified or empty string means ``localhost``.

    * ``port:`` The port of the database server, applicable for PostgreSQL, MySQL, Oracle and Microsoft SQL Server.

        * *Type*: string
        * *Example*: ``'5432'``
        * *Default*: ``''``
        * *Note*: Not specified or empty string means default port.

    * ``dbname:`` The name of the database.

        * *Type*: string
        * *Example*: ``'colvert'`` or ``'db.sqlite3'``
        * *Default*: ``'db.sqlite3'``
        * *Note*: For SQLite, the database name is the path to the database file.

    * ``dbuser:`` The username to connect to the database.

        * *Type*: string
        * *Example*: ``'colvertdbuser'``
        * *Default*: ``''``

    * ``dbuser:`` The username to connect to the database.

        * *Type*: string
        * *Example*: ``'colvertdbuser'``
        * *Default*: ``''``
        * *Note*: For SQLite, the username is not required.

    * ``dbpass:`` The password to connect to the database.

        * *Type*: string
        * *Example*: ``'A 5tr0ng P4ssw0rd!'``
        * *Default*: ``''``
        * *Note*: For SQLite, the password is not required.

    * ``driver:`` The ODBC driver to use for Microsoft SQL Server engine.

        * *Type*: string
        * *Example*: ``'ODBC Driver 17 for SQL Server'``
        * *Default*: ``''``
        * *Note*: Only for Microsoft SQL Server.

.. important::

    When using **Microsoft SQL Server**, ensure you have the correct ODBC driver installed on your system. You can download the ODBC driver from the `Microsoft website <https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server>`_.

    More information concerning Microsoft SQL Server connector and drivers at:
    https://pypi.org/project/django-mssql-backend/

.. admonition:: Testing the connection

    After configuring the settings, you can test the connection by running Django management commands such as ``python manage.py migrate`` to apply migrations to the SQL Server database.

Below are detailed examples about the ``database:`` section that can be set according to the database connection you need.

PostgreSQL
----------

.. code-block:: yaml

    database:
      engine: 'django.db.backends.postgresql'
      host: 'yourdbhost.local'
      port: 'yourdbport'
      dbname: 'yourdbname'
      dbuser: 'yourdbuser'
      dbpass: 'yourdbpassword'

MySQL
-----

.. code-block:: yaml

    database:
      engine: 'django.db.backends.mysql'
      host: 'yourdbhost.local'
      port: 'yourdbport'
      dbname: 'yourdbname'
      dbuser: 'yourdbuser'
      dbpass: 'yourdbpassword'

Oracle
------

.. code-block:: yaml

    database:
      engine: 'django.db.backends.oracle'
      host: 'yourdbhost.local'
      port: 'yourdbport'
      dbname: 'yourdbname'
      dbuser: 'yourdbuser'
      dbpass: 'yourdbpassword'

Microsoft SQL Server
--------------------

.. code-block:: yaml

    database:
      engine: 'sql_server.pyodbc'
      host: 'yourserver\yourinstance'
      port: 'yourinstanceport'
      dbname: 'yourdbname'
      dbuser: 'yourdbuser'
      dbpass: 'yourdbpassword'
      driver: 'ODBC Driver 17 for SQL Server'
