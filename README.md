# Colvert

[![Release](https://img.shields.io/badge/dynamic/json?logo=git&logoColor=white&color=blue&label=Release&query=tag_name&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcolvert-project%2Fcolvert%2Freleases%2Flatest)](https://github.com/colvert-project/colvert/releases/latest)
[![Documentation](https://img.shields.io/badge/Docs-docs.colvert.io-blue?logo=readthedocs&logoColor=white)](https://docs.colvert.io)
[![Licence EUPL-1.2](https://img.shields.io/badge/Licence-EUPL--1.2-blue)](LICENCE)

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

### Key Features

To respond to the needs explained above, **Colvert** offers the following key features:

* _TODO_ - List key features.

### Roadmap

* For now, one **Colvert** instance is dedicated to one constituency. In the future, **Colvert** should be able to manage a relationship between detection use cases and multiple constituencies.
* _TODO_ - Use cases that do not perform well, i.e., that have an unfavorable benefit/effort ratio, need to be improved, redefined, or abandoned. TODO Statistics follow-up?
* _TODO_ Finish list

### Why Colvert?

**D**etection **U**se **C**ase >>> **DUC** >>> DUCK >>> **Colvert** (Mallard duck in French). That's it.

### Links

* **Website:** [colvert.io](https://colvert.io)
* **Git Repository:** `git clone https://github.com/colvert-project/colvert.git`
* **Last Release:** [colvert/releases/latest](https://github.com/colvert-project/colvert/releases/latest)
* _TODO_ **Packages:** [colvert-project/packages](https://github.com/orgs/colvert-project/packages)
* **Docker Registries:**
    * **Docker Hub:** [`TODO`](https://hub.docker.com/r/TODO)
    * **GitHub Container:** [`https://ghcr.io/TODO`](https://ghcr.io/TODO)
* **Issues Tracker:** [colvert/issues](https://github.com/colvert-project/colvert/issues)
* **Discussions:** [colvert-project/discussions](https://github.com/orgs/colvert-project/discussions)
* **Documentation:** [docs.colvert.io](https://docs.colvert.io)

Changelog details are available on the [releases](https://github.com/colvert-project/colvert/releases) page.

## Getting Started

_TODO_
Deploy
how to run code, development and maintenance

Needs a WSGI server

Docker install

_TODO_ Live demo website
    
* + Link in links
* + Link in Intro

### Architecture

[![Python 3.12+](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white&labelColor=3776ab&color=ffd43b)](https://www.python.org)
[![Django 5.1](https://img.shields.io/badge/Django-5.1-white?logo=django&logoColor=white&labelColor=092e20)](https://www.djangoproject.com)
([![Bootstrap 5](https://img.shields.io/badge/Bootstrap-5.3-white?logo=bootstrap&logoColor=white&labelColor=7952b3)](getbootstrap.com))

AdminLTE

**Colvert** is a web application written in **_Python_ 3**, built on **_Django_ 5** web framework with **_AdminLTE 4_** as **_Bootstrap_ 5** template for view and control parts.

**_jQuery_** ._TODO_

_TODO_ Check also with 3.10, 3.11, etc. (recents Python version)

_TODO_ - For all concern about software logic, please refer to the design documentation.
See [DESIGN.md](DESIGN.md) for all technical details.

_TODO_ - git clone doc

### Documentation

[docs.colvert.io](https://docs.colvert.io)

_TODO_ User doc.

_TODO_ Dev. doc.

_TODO_ [DESIGN.md](DESIGN.md)

* Software Lifecycle
    * Design & Technicals
    * CD/CI Ecosystem Status
       * _TODO_ GitHub Status
       * https://www.traviscistatus.com/

_TODO_ Dependencies badge out of date?

_TODO_ NewReleases.io

## Contact

* Feel free to start a topic in discussions part: [colvert-project/discussions](https://github.com/orgs/colvert-project/discussions)
* You can also contact project maintainers via mail: contact@colvert.io

## Security

_TODO_ Advisory

_TODO_ SECURITY.md

* **Security Policy:** [colvert/security/policy](https://github.com/colvert-project/colvert/security/policy)
* **Security Advisories:** [colvert/security/advisories](https://github.com/colvert-project/colvert/security/advisories)

## Contributors

### Author & Project Maintainer

* **styx0x6** <<https://github.com/styx0x6>>

### Contributing Developers

[![styx0x6](https://github.com/styx0x6.png?size=40)](https://github.com/styx0x6)

### Sponsors

[![styx0x6](https://github.com/styx0x6.png?size=40)](https://github.com/styx0x6)

## Licence

[![Licence EUPL-1.2](https://img.shields.io/badge/Licence-EUPL--1.2-blue)](LICENCE)

**Colvert** - The Detection Use Case Management Tool

Copyright &copy; 2024  **The Colvert Contributors** (see [README.md](README.md) / [colvert/settings.py](colvert/settings.py))

Licensed under the EUPL, Version 1.2 only (the "Licence");
You may not use this work except in compliance with the Licence.
You may obtain a copy of the Licence, available in the 23 official
languages of the European Union, at:

https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

##

[Colvert Logo](https://github.com/colvert-project/colvert/tree/main/rsc/logo) &copy; 2024 by [Colvert Project Team](https://github.com/colvert-project) is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/?ref=chooser-v1) <img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt="CC" width="16" height="16" /><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt="BY" width="16" height="16" /><img src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt="SA" width="16" height="16" />

![CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/4.0/80x15.png)

## Credits

Credits are listed in [documentation](https://docs.colvert.io). _TODO_ Set exact link.