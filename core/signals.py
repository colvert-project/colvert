"""
Colvert - The Detection Use Case Management Tool
Copyright (C) 2024-2025  The Colvert Contributors (see README.md / colvert/settings.py)

Licensed under the EUPL, Version 1.2 only (the "Licence");
You may not use this work except in compliance with the Licence.
You may obtain a copy of the Licence, available in the 23 official
languages of the European Union, at:
https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12
"""

from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models.usecase import Severity, Status
from django.contrib.auth.models import User
from django.conf import settings

@receiver(post_migrate)
def add_default_values(sender, **kwargs):
    """Add default values to the database after the migration.

    Default values added for the following models:
        - Severity
        - Status
    and create the default admin user.
    """
    if sender.name == 'core':
        default_severities = [
            {'name': 'Low'},
            {'name': 'Medium'},
            {'name': 'High'},
        ]
        for severity in default_severities:
            Severity.objects.get_or_create(**severity)

        default_status = [
            {'name': 'Idea to Design'},
            {'name': 'Design in Progress'},
            {'name': 'Ready to be Implemented'},
            {'name': 'Requested for Implementation'},
            {'name': 'Implementation in Progress'},
            {'name': 'Ready for Testing'},
            {'name': 'Testing in Progress'},
            {'name': 'Deployed'},
            {'name': 'On Hold'},
            {'name': 'Removed'},
        ]
        for status in default_status:
            Status.objects.get_or_create(**status)
        
        # Create the default admin user
        User.objects.create_superuser(username=getattr(settings, 'DEFAULT_ADMIN_USER'), password=getattr(settings, 'DEFAULT_ADMIN_PASSWORD'))
        # TODO: Django logger #print("Default values added successfully.")
