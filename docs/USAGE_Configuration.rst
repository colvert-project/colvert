########################
How to Configure Colvert
########################

If it doesn't exist already (a.k.a. at the first run), Colvert will create `colvert.yml` configuration file with defaults settings.

You can modify the settings in the `colvert.yml` file to suit your requirements.

.. note::

    You can also reset the configuration to the default settings by deleting the `colvert.yml` file and restarting the application, or by copying the `colvert.template.yml` file to `colvert.yml`.

Settings
--------

The `colvert.yml` file must be set with the following configuration settings:

**TODO** REVIEW RST FORMAT BELOW

- **debug**: Enables or disables debug mode.
  - Type: string
  - Values: 'true' or 'false'
    - Default: 'false'

- **allowed-hosts**: A list of strings representing the host/domain names that Colvert can serve.
    - Type: list of strings
    - Example: ['yourdomain.com', 'www.yourdomain.com']

- **csrf-trusted-origins**: A list of trusted origins for CSRF protection.
    - Type: list of strings
    - Example: ['https://yourdomain.com', 'https://www.yourdomain.com']

- **database**: Database configuration settings.
    - **engine**: The database backend to use.
        - Type: string
        - Example: 'django.db.backends.postgresql'
    - **host**: The host of the database server.
        - Type: string
        - Example: 'dbserver.local' or 'dbcluster\dbinstance' for MS SQL
    - **port**: The port of the database server.
        - Type: string
        - Example: '5432' or ('' | no definition) for MS SQL default port
    - **dbname**: The name of the database.
        - Type: string
        - Example: 'colvert'
    - **dbuser**: The username to connect to the database.
        - Type: string
        - Example: 'colvertuser'
    - **dbpass**: The password to connect to the database.
        - Type: string
        - Example: 'A 5tr0ng P4ssw0rd!'
    - **driver**: *ONLY FOR MS SQL* - The ODBC driver to use for Microsoft SQL Server.
        - Type: string
        - Example: 'ODBC Driver 17 for SQL Server'

colvert.yml
===========

`colvert.yml` example:

.. code-block:: yaml

    # Colvert's configuration

    debug: 'false'
    allowed-hosts:
      - 'yourdomain.com'
      - 'www.yourdomain.com'
    csrf-trusted-origins:
      - 'https://yourdomain.com'
      - 'https://www.yourdomain.com'
    database:
      engine: 'django.db.backends.sqlite3'
      dbname: 'db.sqlite3'

By default, Colvert uses the SQLite local database. You can change the database settings to use other databases such as PostgreSQL, MySQL, Oracle or Microsoft SQL Server.

The `database` section can be set as below according to the database connection you need.

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
      [port: 'yourinstanceport'] # Not specified or empty string means default port
      dbname: 'yourdbname'
      dbuser: 'yourdbuser'
      dbpass: 'yourdbpassword'
      driver: 'ODBC Driver 17 for SQL Server'

**TODO** Manage all possible version of drivers in docs
String. ODBC Driver to use ("ODBC Driver 13 for SQL Server", "SQL Server Native Client 11.0", "FreeTDS" etc). Default is "ODBC Driver 13 for SQL Server".
# Ensure you have the correct ODBC driver installed on your system.

.. important::

    When using **Microsoft SQL Server**, you need to install the ODBC Driver 17 for SQL Server on your system.

    You can download the ODBC Driver 17 for SQL Server from the `Microsoft website <https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server>`_.

.. note::

    **Testing the Connection**: After configuring the settings, you can test the connection by running Django management commands such as `python manage.py migrate` to apply migrations to the SQL Server database.

.. seealso::

    More information concerning Microsoft SQL Server connector at https://pypi.org/project/django-mssql-backend/.
