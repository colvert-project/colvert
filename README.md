# Colvert

[![Release](https://img.shields.io/badge/dynamic/json?logo=git&logoColor=white&color=blue&label=Release&query=tag_name&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fcolvert-project%2Fcolvert%2Freleases%2Flatest)](https://github.com/colvert-project/colvert/releases/latest)
[![Documentation](https://img.shields.io/badge/Docs-docs.colvert.io-blue?logo=readthedocs&logoColor=white)](https://docs.colvert.io)
[![Licence EUPL-1.2](https://img.shields.io/badge/Licence-EUPL--1.2-blue)](LICENCE)

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
    * From idea to organized and prioritized development
    * Map local ideas and needs to those provided by connectors
    * _Synchronize_ detection use cases with providers catalogs
    *  on use cases
    * Use cases _scoring_ for priorization
    * Add full rich-text documentation and additional _more-valued data fields_ as:
      * _Runbooks_ for security analysts
      * Implemented queries
    * Add _Custom Lists_ (Whitelists, Thresholds, Scope, etc.)
    * Attach external documents or reference to
    * Development status

### Roadmap

* Scoring System
* Connectors
* Source Logs
* For now, one **Colvert** instance is dedicated to one constituency. In the future, **Colvert** should be able to manage a relationship between detection use cases and multiple constituencies.
* Metrics about use cases that do not perform well, i.e., that have an unfavorable benefit/effort ratio, need to be improved, redefined, or abandoned.

### Why Colvert?

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

All topics about installation / deployment / usage / design / architecture / etc. can be found in [**documentation**](https://docs.colvert.io).

## Security

* **Security Policy:** [colvert/security/policy](https://github.com/colvert-project/colvert/security/policy)
* **Security Advisories:** [colvert/security/advisories](https://github.com/colvert-project/colvert/security/advisories)

## Contact

* Feel free to start a topic in discussions part: [colvert-project/discussions](https://github.com/orgs/colvert-project/discussions)
* You can also contact project maintainers via mail: contact@colvert.io

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

Credits are listed in [docs/Credits](https://docs.colvert.io/Credits.html).