"""
Colvert - The Detection Use Case Management Tool
Copyright (C) 2024  The Colvert Contributors (see README.md / colvert/settings.py)

Licensed under the EUPL, Version 1.2 only (the "Licence");
You may not use this work except in compliance with the Licence.
You may obtain a copy of the Licence, available in the 23 official
languages of the European Union, at:
https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12
"""

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError

# Constants
UC_ENTRIES_LIMIT = 9999 # Limit of entries in the UseCase table
UC_RELATED_NAME = 'usecases' # Related name for the UseCase model in the related models
UC_DISPLAY_NULL = "Not Defined" # Display value for null values in the UseCase model

class Category(models.Model):
    """
    Represents a use case category in the database.
    """
    # Default: id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    meta_origin = models.CharField(max_length=100, default=getattr(settings, "APP_TECH_NAME"))
    meta_created_at = models.DateTimeField(auto_now_add=True, editable=False) # Automatically set the field to now when the object is first created
    meta_modified_at = models.DateTimeField(auto_now=True, editable=False) # Automatically set the field to now every time the object is saved

class Scope(models.Model):
    """
    Represents a use case scope in the database.
    """
    # Default: id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    meta_origin = models.CharField(max_length=100, default=getattr(settings, "APP_TECH_NAME"))
    meta_created_at = models.DateTimeField(auto_now_add=True, editable=False) # Automatically set the field to now when the object is first created
    meta_modified_at = models.DateTimeField(auto_now=True, editable=False) # Automatically set the field to now every time the object is saved

class Severity(models.Model):
    """
    Represents a use case severity in the database.
    Default Severity values are defined and set in the 'signals.py' file.
    """
    # Default: id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    meta_origin = models.CharField(max_length=100, default=getattr(settings, "APP_TECH_NAME"))
    meta_created_at = models.DateTimeField(auto_now_add=True, editable=False) # Automatically set the field to now when the object is first created
    meta_modified_at = models.DateTimeField(auto_now=True, editable=False) # Automatically set the field to now every time the object is saved

class Status(models.Model):
    """
    Represents a use case local status in the database.
    Default Status values are defined and set in the 'signals.py' file.
    """
    # Default: id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    meta_origin = models.CharField(max_length=100, default=getattr(settings, "APP_TECH_NAME"))
    meta_created_at = models.DateTimeField(auto_now_add=True, editable=False) # Automatically set the field to now when the object is first created
    meta_modified_at = models.DateTimeField(auto_now=True, editable=False) # Automatically set the field to now every time the object is saved

class UseCase(models.Model):
    """
    Represents a use case in the database.
    Limited to UC_ENTRIES_LIMIT entries.
    """
    # Default: id = models.AutoField(primary_key=True)
    uc_title = models.TextField()
    uc_reference = models.CharField(max_length=100)
    uc_description = models.TextField()
    uc_comments = models.TextField()
    uc_release_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    uc_Category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name=UC_RELATED_NAME)
    uc_Category_name = models.CharField(max_length=100, editable=False, default=UC_DISPLAY_NULL) # Store the category name for resilience display purposes
    uc_Scope_id = models.ForeignKey(Scope, on_delete=models.SET_NULL, null=True, related_name=UC_RELATED_NAME)
    uc_Scope_name = models.CharField(max_length=100, editable=False, default=UC_DISPLAY_NULL) # Store the scope name for resilience display purposes
    uc_Severity_id = models.ForeignKey(Severity, on_delete=models.SET_NULL, null=True, related_name=UC_RELATED_NAME)
    uc_Severity_name = models.CharField(max_length=20, editable=False, default=UC_DISPLAY_NULL) # Store the severity name for resilience display purposes
    uc_247_possible = models.BooleanField(default=False)
    uc_247_activated = models.BooleanField(default=False)
    uc_origin_status = models.CharField(max_length=100, null=True)
    local_Status_id = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, related_name=UC_RELATED_NAME)
    local_Status_name = models.CharField(max_length=50, editable=False, default=UC_DISPLAY_NULL) # Store the status name for resilience display purposes
    uc_triggered_occurances = models.IntegerField(default=0)
    uc_last_triggered_at = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    # TODO: 2
    local_impl_expected_at = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    # TODO: ExtUCImplementationADUserSIDAssignedTo char(47)
    # TODO: ExtUCImplementationDisplayAssignedTo varchar(65535)
    local_impl_major_priority = models.BooleanField(default=False)
    local_doc_objective = models.TextField()
    local_doc_requirements = models.TextField(blank=True, null=True)
    local_doc_comments = models.TextField(blank=True, null=True)
    # TODO: Review/redesign the use of the local_doc_* fields below, they may be better stored in a separate table
    local_doc_testing_method = models.TextField(blank=True, null=True)
    local_doc_normal_situation = models.TextField(blank=True, null=True)
    local_doc_abnormal_situation = models.TextField(blank=True, null=True)
    local_doc_detection_criteria = models.TextField(blank=True, null=True)
    local_doc_alt_detection_criteria = models.TextField(blank=True, null=True)
    local_doc_detection_limitations = models.TextField(blank=True, null=True)
    local_doc_response = models.TextField(blank=True, null=True)
    local_doc_queries = models.TextField(blank=True, null=True)
    #TODO: Needed? local_doc_playbook = models.TextField(blank=True, null=True)
    meta_last_sync_origin = models.CharField(max_length=100, default=getattr(settings, "APP_TECH_NAME"))
    meta_first_origin = models.CharField(max_length=100, editable=False)
    meta_created_at = models.DateTimeField(auto_now_add=True, editable=False) # Automatically set the field to now when the object is first created
    meta_modified_at = models.DateTimeField(auto_now=True, editable=False) # Automatically set the field to now every time the object is saved
    meta_ucfields_metadata = models.JSONField(default=dict, editable=False) # Store fields metadata

    @property
    def get_display_id(self):
        """
        Returns the use case ID in a human-readable format (eg. 0084).
        """
        return f"{self.id:04d}"

    def save(self, *args, **kwargs):
        """
        Override the save method to:
        - Limit the number of entries in the UseCase table, in order to keep it coherent
        with the display_id property, the maximum number of entries is set to 9999.
        - Automatically set the uc_Category_name, uc_Scope_name, uc_Severity_name and local_Status_name fields.
        - Set meta_first_origin field and force it to rest as the first value set.
        - Update synchronizable use case fields metadata (only fields starting with 'uc_').

        Raises:
            ValidationError: If the number of entries in the UseCase table exceeds ENTRIES_LIMIT.
        """
        # Limit the number of entries in the UseCase table
        if UseCase.objects.count() >= UC_ENTRIES_LIMIT:
            raise ValidationError("Cannot add more than {} entries to the UseCase table.".format(UC_ENTRIES_LIMIT))
        
        # Set the category, scope, severity and local status name based on the foreign key
        if self.uc_Category_id:
            self.uc_Category_name = self.uc_Category_id.name
        if self.uc_Scope_id:
            self.uc_Scope_name = self.uc_Scope_id.name
        if self.uc_Severity_id:
            self.uc_Severity_name = self.uc_Severity_id.name
        if self.local_Status_id:
            self.local_Status_name = self.local_Status_id.name
        
        # Manage meta_first_origin field
        # Check if the object already exists (i.e., it's being updated)
        if self.pk:
            original = UseCase.objects.get(pk=self.pk)
            # If meta_first_origin already has a value (shall be yes), prevent changes
            if original.meta_first_origin:
                self.meta_first_origin = original.meta_first_origin
        # Else set it the first time
        else:
            self.meta_first_origin = self.meta_last_sync_origin

        # Update 'uc_' fields metadata each time they are modified
        # First case, the object already exists (i.e., it's being updated)
        if self.pk:
            original = UseCase.objects.get(pk=self.pk)

            for field in self._meta.fields:
                if field.name.startswith('uc_'):
                    # The field is being updated with a new value
                    if self.get_value(field.name) != original.get_value(field.name):
                        self.meta_ucfields_metadata[field.name] = {
                            "field_last_sync_origin": self.meta_last_sync_origin,
                            "field_modified_at": timezone.now().isoformat(),
                        }
        # Second case, if the object is new, jsut set metadata for the given 'uc_' field
        elif field.name.startswith('uc_'):
            self.meta_ucfields_metadata[field.name] = {
                "field_last_sync_origin": self.meta_last_sync_origin,
                "field_modified_at": timezone.now().isoformat(),
            }

        super().save(*args, **kwargs)
    