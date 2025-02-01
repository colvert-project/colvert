# Colvert

[![Release](https://img.shields.io/badge/dynamic/json?logo=git&logoColor=white&color=blue&label=Release&query=tag_name&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcolvert-project%2Fcolvert%2Freleases%2Flatest)](https://github.com/colvert-project/colvert/releases/latest)
[![Documentation](https://img.shields.io/badge/Docs-docs.colvert.io-blue?logo=readthedocs&logoColor=white)](https://docs.colvert.io)
[![Licence EUPL-1.2](https://img.shields.io/badge/Licence-EUPL--1.2-blue)](LICENCE)

[![Python 3.12+](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white&labelColor=3776ab&color=ffd43b)](https://www.python.org/)
[![Django 5](https://img.shields.io/badge/Django-5-white?logo=django&logoColor=white&labelColor=092e20)](https://www.djangoproject.com/)
[![Bootstrap 5](https://img.shields.io/badge/Bootstrap-5-white?logo=bootstrap&logoColor=white&labelColor=7952b3)](https://getbootstrap.com/)
[![AdminLTE 4](https://img.shields.io/badge/AdminLTE-4-white?logo=bootstrap&logoColor=white&labelColor=grey)](https://adminlte.io/)

**Colvert** is a tool made for cybersecurity teams (CSIRTs / SOCs) and designed to manage their portfolio of _detection use cases_ through their entire lifecycle in the context of **Information Security Event Management**.

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

* **Dashboards**
* **Detection Use Cases Management**
  * **Add / Modify / Delete** Detection Use Cases
    * Status from idea to implementation through organized and prioritized development.
    * Use cases _scoring_ for priorization.
    * Enhance detection use cases with contextual data provided by connectors.
    * _Synchronize_ detection use cases with providers catalogs.
    * Add full rich-text documentation and additional _more-valued data fields_ as:
      * _Runbooks_ for security analysts.
      * Implemented queries.
    * Add _Custom Lists_ (Whitelists, Thresholds, Scope, etc.).
    * Attach external documents or references to.

### Roadmap

* Scoring System.
* Connectors.
* Source Logs.
* For now, one **Colvert** instance is dedicated to one constituency. In the future, **Colvert** might be able to manage a relationship between detection use cases and multiple constituencies with also dedicated use cases by constituancy.
* Metrics about use cases that do not perform well, i.e., that have an unfavorable benefit/effort ratio, need to be improved, redefined, or abandoned.

### Why Colvert?

From a very long brainstorming:

**D**etection **U**se **C**ase >>> **DUC** >>> DUCK >>> **Colvert** (Mallard duck in French).

That's it.

### Links

* **Website:** [colvert.io](https://colvert.io)
* **Documentation:** [docs.colvert.io](https://docs.colvert.io)
* **Git Repository:** `git clone https://github.com/colvert-project/colvert.git`
* **Last Release:** [colvert/releases/latest](https://github.com/colvert-project/colvert/releases/latest)
* **Packages:** [colvert-project/packages](https://github.com/orgs/colvert-project/packages)
* **Discussions:** [colvert-project/discussions](https://github.com/orgs/colvert-project/discussions)
* **Issues Tracker:** [colvert/issues](https://github.com/colvert-project/colvert/issues)

Changelog details are available on the [releases](https://github.com/colvert-project/colvert/releases) page.

All topics about installation / deployment / usage / design / architecture / contribution / etc. can be found in [**documentation**](https://docs.colvert.io).

## Security

* **Security Policy:** [colvert/security/policy](https://github.com/colvert-project/colvert/security/policy)
* **Security Advisories:** [colvert/security/advisories](https://github.com/colvert-project/colvert/security/advisories)

## Contact

* Feel free to start a topic in discussions part: [colvert-project/discussions](https://github.com/orgs/colvert-project/discussions)
* You can also contact project maintainers via mail: <contact@colvert.io>

## Contributors

### Author & Project Maintainer

* **styx0x6** <<https://github.com/styx0x6>>

[![styx0x6](https://github.com/styx0x6.png?size=40)](https://github.com/styx0x6)

### Contributing Developers

.

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

<https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12>

##

![CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/4.0/80x15.png)

[Colvert Logo](https://github.com/colvert-project/colvert/tree/main/rsc/logo) &copy; 2024 by [Colvert Project Team](https://github.com/colvert-project) is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/?ref=chooser-v1)

## Credits

Credits are listed in [docs/Credits](https://docs.colvert.io/Credits.html).
