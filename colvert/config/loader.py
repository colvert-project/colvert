"""
Colvert - The Detection Use Case Management Tool
Copyright (C) 2025  The Colvert Contributors (see README.md / colvert/settings.py)

Licensed under the EUPL, Version 1.2 only (the "Licence");
You may not use this work except in compliance with the Licence.
You may obtain a copy of the Licence, available in the 23 official
languages of the European Union, at:
https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

Colvert's configuration load from colvert.yml or colvert.yaml file
"""

import os
from pathlib import Path
import yaml
from django.core.management.utils import get_random_secret_key

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULTS_DIR = os.path.join(BASE_DIR, 'colvert', 'config', 'defaults')

# Configuration file paths
TEMPLATE_PATH = os.path.join(DEFAULTS_DIR, 'colvert.template.yml')
CONFIG_YML_PATH = os.path.join(BASE_DIR, 'colvert.yml')
CONFIG_YAML_PATH = os.path.join(BASE_DIR, 'colvert.yaml')
SECRET_KEY_PATH = os.path.join(BASE_DIR, 'SECRET_KEY')

class ColvertConfig:
    """Colvert's configuration class to load settings from 'colvert.yml' or 'colvert.yaml', and 'SECRET_KEY' files.
    """

    def __init__(self):
        """Initialize Colvert's configuration settings with default values, 
        then load configuration settings from 'colvert.yml' or 'colvert.yaml', and 'SECRET_KEY' files.
        If not possible for any reason, we keep default set values.
        """
        # Check first if files exist and generate them if necessary
        try:
            self._check_config_files()
        except FileNotFoundError as e:
            # TODO: Log error (logger.error(e)?), check Django logger
            pass
        
        # Load SECRET_KEY value
        self._secret_key = self._load_secret_key()

        # Default configuration settings
        self._yml_org_name = 'Colvert'
        self._yml_org_logo = os.path.join(DEFAULTS_DIR, 'org_180px.png')
        self._yml_debug = False
        self._yml_allowed_hosts = ['*']
        self._yml_csrf_trusted_origins = ['http://', 'https://']
        self._yml_database = {
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": f"{BASE_DIR}/db.sqlite3",
            }
        }
        # Load configuration settings from YAML configuration file
        yaml_config = self._load_yaml_config()
        if yaml_config:
            for key, value in yaml_config.items():
                if key == 'org-name':
                    self._yml_org_name = str(value)
                elif key == 'org-logo':
                    # Given file if it exists
                    if os.path.exists(os.path.join(BASE_DIR, str(value))):
                        self._yml_org_logo = os.path.join(BASE_DIR, str(value))
                    else:
                        self._yml_org_logo = os.path.join(DEFAULTS_DIR, 'org_180px.png')
                elif key == 'debug':
                    self._yml_debug = str(value).lower() == 'true'
                elif key == 'allowed-hosts':
                    self._yml_allowed_hosts = [str(host) for host in value]
                elif key == 'csrf-trusted-origins':
                    self._yml_csrf_trusted_origins = [str(origin) for origin in value]
                elif key == 'database':
                    if str(value['engine']) == 'django.db.backends.sqlite3':
                        # Set SQLite3 database settings
                        self._yml_database = {
                            "default": {
                                "ENGINE": str(value['engine']),
                                "NAME": f"{BASE_DIR}/{str(value.get('dbname', 'db.sqlite3'))}",
                            }
                        }
                    elif str(value['engine']) in ['django.db.backends.postgresql', 'django.db.backends.mysql', 'django.db.backends.oracle']:
                        # Set database settings
                        self._yml_database = {
                            "default": {
                                "ENGINE": str(value['engine']),
                                "HOST": str(value.get('host', '')),
                                "PORT": str(value.get('port', '')),
                                "NAME": str(value.get('dbname', '')),
                                "USER": str(value.get('dbuser', '')),
                                "PASSWORD": str(value.get('dbpass', '')),
                            }
                        }
                    elif str(value['engine']) == 'sql_server.pyodbc':
                        self._yml_database = {
                            "default": {
                                "ENGINE": str(value['engine']),
                                "HOST": str(value.get('host', '')),
                                "PORT": str(value.get('port', '')),
                                "NAME": str(value.get('dbname', '')),
                                "USER": str(value.get('dbuser', '')),
                                "PASSWORD": str(value.get('dbpass', '')),
                                "OPTIONS": {
                                    "driver": str(value.get('driver', '')),
                                }
                            }
                        }

    def _check_config_files(self) -> None:
        """Check configuration files and generate them if they don't exist.

        Copy 'colvert.yml' from 'colvert.template.yml' file if neither 'colvert.yml' nor 'colvert.yaml' exist.
        Generate 'SECRET_KEY' file with a new random secret key if it doesn't exist.

        :raises FileNotFoundError: If 'colvert.template.yml' file is not found.
        :raises FileNotFoundError: If SECRET_KEY file is not found.
        """
        if not (os.path.exists(CONFIG_YML_PATH) or os.path.exists(CONFIG_YAML_PATH)):
            if os.path.exists(TEMPLATE_PATH):
                with open(TEMPLATE_PATH, 'r') as t_file:
                    with open(CONFIG_YML_PATH, 'w') as c_file:
                        c_file.write(t_file.read())
            else:
                raise FileNotFoundError(f"Template file not found: {TEMPLATE_PATH}")

        if not (os.path.exists(SECRET_KEY_PATH)):
            with open(SECRET_KEY_PATH, 'w') as s_file:
                s_file.write(get_random_secret_key())
        else:
            raise FileNotFoundError(f"Secret key file not found: {SECRET_KEY_PATH}")

    def _load_yaml_config(self) -> dict:
        """Load configuration settings from 'colvert.yml' or 'colvert.yaml' file.

        :return: Configuration settings loaded from the file or None value if impossible.
        :rtype: dict
        """
        yaml_config = None
        if os.path.exists(CONFIG_YML_PATH):
            with open(CONFIG_YML_PATH, 'r') as config_file:
                yaml_config = yaml.safe_load(config_file)
        elif os.path.exists(CONFIG_YAML_PATH):
            with open(CONFIG_YAML_PATH, 'r') as config_file:
                yaml_config = yaml.safe_load(config_file)
        return yaml_config

    def _load_secret_key(self) -> str:
        """Load SECRET_KEY value from 'SECRET_KEY' file. Generate a new random secret key if the file doesn't exist.

        :return: SECRET_KEY value loaded from file or a generated random secret key if impossible.
        :rtype: str
        """
        secret_key_value = get_random_secret_key()
        if os.path.exists(SECRET_KEY_PATH):
            with open(SECRET_KEY_PATH, 'r') as secret_key_file:
                secret_key_value = secret_key_file.read()
        return secret_key_value

    @property
    def secret_key(self) -> str:
        return self._secret_key

    @property
    def org_name(self) -> str:
        return self._yml_org_name

    @property
    def org_logo(self) -> str:
        return self._yml_org_logo

    @property
    def debug(self) -> bool:
        return self._yml_debug

    @property
    def allowed_hosts(self) -> list:
        return self._yml_allowed_hosts

    @property
    def csrf_trusted_origins(self) -> list:
        return self._yml_csrf_trusted_origins

    @property
    def database(self) -> dict:
        return self._yml_database
