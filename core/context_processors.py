"""
Colvert - The Detection Use Case Management Tool
Copyright (C) 2025  The Colvert Contributors (see README.md / colvert/settings.py)

Licensed under the EUPL, Version 1.2 only (the "Licence");
you may not use this work except in compliance with the Licence.
You may obtain a copy of the Licence, available in the 23 official
languages of the European Union, at:
https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12
"""

from django.conf import settings


def global_context(request):
    """Provide global placeholders used by base templates."""
    return {
        "pl_lang": settings.LANGUAGE_CODE,
        "pl_charset": settings.DEFAULT_CHARSET,
        "pl_description": f"{settings.APP_SHORT_NAME} - {settings.APP_DESC}",
        "pl_contributors": settings.APP_CONTRIBUTORS,
        "pl_licence": settings.APP_LICENCE,
        "pl_help": settings.APP_URL_ISSUES,
        "pl_powered_by": settings.APP_POWERED_BY,
        "pl_title": settings.TITLE_PREFIX,
        "pl_short_name": settings.APP_SHORT_NAME,
        "pl_footer": settings.APP_COPYRIGHT_STRING,
    }


def instance_context(request):
    """Provide instance-level placeholders used by app templates."""
    return {
        "pl_app_company": settings.ORG_NAME,
        "pl_org_logo": settings.ORG_LOGO,
    }
