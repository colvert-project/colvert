# Colvert

![Version 0.1.0](https://img.shields.io/badge/Version-0.1.0-chartreuse?logo=git&logoColor=white)
[![Python 3.12+](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white&labelColor=3776ab&color=ffd43b)](https://www.python.org)
[![Licence EUPL-1.2](https://img.shields.io/badge/Licence-EUPL--1.2-blue)](LICENCE)

_TODO_ Check also with 3.10, 3.11, etc. (recents Python version)

**Colvert** is a tool designed to manage your portfolio of _detection use cases_ through their entire lifecycle in the context of **Information Security Event Management**.

## About

### Purpose

**Colvert** manage the portfolio of _detection use cases_ with the possibility to document and follow-up use cases development, improvement and implementation; testing status; risk coverage compared to well-known security threats based on multiple contextual data sources; related preventive controls; and instructions for analysts triage, qualification, and correlation as playbooks and Standard Operating Procedures (SOPs).
It is designed to be used in the context of the _Service Area_ **Information Security Event Management** / _Service_ **Monitoring and Detection** / _Function_ **Detection Use Case Management** as defined in the [CSIRT Services Framework Version 2.1](https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2.1) from the [FIRST](https://www.first.org):

> _**Purpose:**_ Manage the portfolio of detection use cases through their entire lifecycle.
> 
> _**Description:**_ New detection approaches are developed, tested, and improved, and eventually onboarded into a detection use case in production. Instructions for analyst triage, qualification, and correlation need to be developed, for example in the form of playbooks and Standard Operating Procedures (SOPs). Use cases that do not perform well, i.e., that have an unfavorable benefit/effort ratio, need to be improved, redefined, or abandoned. The portfolio of detection use cases should be expanded in a risk-oriented way and in coordination with preventive controls.
> 
> _**Outcome:**_ A portfolio of effective detection use cases that are relevant to the constituency is developed.

### Features

In order to respond to the needs explained above, **Colvert** offers the following features:

* _TODO_ - List features.

### Roadmap

_TODO_ - Link to project.
_TODO_ - Put list below in project.

* For now, one **Colvert** instance is dedicated to one constituency. In the future, **Colvert** should be able to manage a relationship between detection use cases and multiple constituencies.
* _TODO_ - Use cases that do not perform well, i.e., that have an unfavorable benefit/effort ratio, need to be improved, redefined, or abandoned. TODO Statistics follow-up?

### Architecture

**Colvert** is a web application written in **_Python_**, built on **_Django_** web framework using _SQLAlchemy_ for database and model management, some extensions for additional _Flask_ features, **_Bootstrap_** & **_jQuery_** for view and control parts._TODO_

_TODO_ - For all concern about software logic, please refer to the design documentation.
See [DESIGN.md](DESIGN.md) for all technical details.

_TODO_ - git clone doc

## Getting Started

_TODO_
Deploy
how to run code, development and maintenance

Needs a WSGI server

## Software Lifecycle

### Development

* `master` branch

_TODO_ Dependencies badge out of date?

### Design & Technicals

_TODO_ [DESIGN.md](DESIGN.md)

### Changelog

All change details are listed into _TODO_ [CHANGELOG.md](CHANGELOG.md).

## Contributors

* styx0x6 <<https://github.com/styx0x6>>

## Security

_TODO_ Advisory

_TODO_ SECURITY.md

## Licence

**Colvert** - The Detection Use Case Management Tool

Copyright &copy; 2024  **The Colvert Contributors** (see [README.md](README.md) / [colvert/settings.py](colvert/settings.py))

Licensed under the EUPL, Version 1.2 only (the "Licence");
You may not use this work except in compliance with the Licence.
You may obtain a copy of the Licence, available in the 23 official
languages of the European Union, at:

https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

##

[Colvert Logo](https://github.com/colvert-project/colvert/tree/main/rsc/logo) &copy; 2024 by [Colvert Project Team](https://github.com/colvert-project) is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/?ref=chooser-v1) <img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="CC" width="16" height="16" /><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt="BY" width="16" height="16" /><img src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt="SA" width="16" height="16" />

## Credits

Credits are listed in _TODO_ [DESIGN.md](DESIGN.md).