"""
Colvert - The Detection Use Case Management Tool
Copyright (C) 2024  The Colvert Contributors (see README.md / colvert/settings.py)

Licensed under the EUPL, Version 1.2 only (the "Licence");
You may not use this work except in compliance with the Licence.
You may obtain a copy of the Licence, available in the 23 official
languages of the European Union, at:
https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboards, name='root'),
    path('home/', views.dashboards, name='home'),
    path('dashboards/', views.dashboards, name='dashboards'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
]
