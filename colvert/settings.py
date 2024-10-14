"""
Colvert - The Detection Use Case Management Tool
Copyright (C) 2024  The Colvert Contributors (see README.md / colvert/settings.py)

Licensed under the EUPL, Version 1.2 only (the "Licence");
You may not use this work except in compliance with the Licence.
You may obtain a copy of the Licence, available in the 23 official
languages of the European Union, at:
https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12


Django settings for colvert project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-@m)cs(idp(tvf_*aia)$i($xm%+(4g2@m6n+q-c!!c_3+r_d2b"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "colvert.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "colvert.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Colvert - Application constants

APP_TECH_NAME = "colvert"
APP_SHORT_NAME = "Colvert"
APP_SUB_NAME = "The Detection Use Case Management Tool"
APP_DESC = "Manage your detection use cases portfolio"
APP_LONG_DESC = "Manage your portfolio of detection use cases with the possibility to document and follow-up use cases development, improvement and implementation; testing status; risk coverage compared to well-known security threats based on multiple contextual data sources; related preventive controls; and instructions for analysts triage, qualification, and correlation as playbooks and Standard Operating Procedures (SOPs)."
APP_CONTRIBUTORS = "styx0x6 <https://github.com/styx0x6>"
APP_SPONSOR = "Maybe you"
APP_LICENCE = "EUPL-1.2"
APP_MAIL_CONTACT = "contact@colvert.io"
APP_URL_WEBSITE = "https://colvert.io"
APP_URL_GIT = "https://github.com/colvert-project/colvert.git"
APP_URL_LAST_RELEASE = "https://github.com/colvert-project/colvert/releases/latest"
APP_URL_ISSUES = "https://github.com/colvert-project/colvert/issues"
APP_URL_TOPICS = "https://github.com/orgs/colvert-project/discussions"
APP_URL_DOCS = "https://docs.colvert.io"
APP_URL_SECURITY_POLICY = "https://github.com/colvert-project/colvert/security/policy"
APP_URL_SECURITY_ADVISORIES = "https://github.com/colvert-project/colvert/security/advisories"
APP_CONTRIBUTING_MD = "CONTRIBUTING.md"
APP_COC_MD = "CODE_OF_CONDUCT.md"
APP_POWERED_BY = "Django+AdminLTE"
APP_VERSION = "0.1.0"
APP_YEARS = "2024"
APP_VERSION_STRING = "%s/%s" % (APP_TECH_NAME, APP_VERSION)
APP_COPYRIGHT_STRING = "Copyright (C) %s  %s. %s." % (APP_YEARS, APP_CONTRIBUTORS, APP_LICENCE)
APP_COPYRIGHT_HTML = "Copyright &copy; %s %s. Licensed under the %s." % (APP_YEARS, APP_CONTRIBUTORS, APP_LICENCE)
