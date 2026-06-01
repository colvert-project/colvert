"""
Colvert - The Detection Use Case Management Tool
Copyright (C) 2024  The Colvert Contributors (see README.md / colvert/settings.py)

Licensed under the EUPL, Version 1.2 only (the "Licence");
you may not use this work except in compliance with the Licence.
You may obtain a copy of the Licence, available in the 23 official
languages of the European Union, at:
https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12
"""

from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET, require_http_methods, require_POST


def _auth_response(success: bool, message: str, status: int, **extra) -> JsonResponse:
    payload = {
        "success": success,
        "message": message,
    }
    payload.update(extra)
    return JsonResponse(payload, status=status)


@require_http_methods(["GET", "POST"])
def signin(request):
    if request.user.is_authenticated:
        return redirect("dashboards")

    form = AuthenticationForm(request=request, data=request.POST or None)
    signin_msg = None

    if request.method == "POST":
        if form.is_valid():
            login(request, form.get_user())
            return redirect("dashboards")
        signin_msg = "Invalid username or password."

    context = {
        "pl_title": f"{settings.TITLE_PREFIX} - Sign In",
        "pl_signin_base_route": reverse("signin"),
        "pl_signin_api_route": reverse("signin_api"),
        "pl_signin_msg": signin_msg,
        "pl_signin_short_name": settings.APP_SHORT_NAME,
        "pl_signin_footer": settings.APP_COPYRIGHT_STRING,
        "pl_signin_form": form,
    }
    return render(request, "signin.html", context)


@require_POST
def signin_api(request):
    if request.user.is_authenticated:
        return _auth_response(
            True,
            "Already authenticated.",
            200,
            redirect_url=reverse("dashboards"),
        )

    form = AuthenticationForm(request=request, data=request.POST)
    if not form.is_valid():
        return _auth_response(
            False,
            "Invalid username or password.",
            400,
            errors=form.errors.get_json_data(escape_html=True),
        )

    login(request, form.get_user())
    return _auth_response(
        True,
        "Authenticated successfully.",
        200,
        redirect_url=reverse("dashboards"),
    )


@require_http_methods(["GET", "POST"])
def signout(request):
    logout(request)
    return redirect("signin")


@require_POST
def signout_api(request):
    logout(request)
    return _auth_response(
        True,
        "Signed out successfully.",
        200,
        redirect_url=reverse("signin"),
    )


@login_required
@require_GET
def dashboards(request):
    context = {
        "pl_title": f"{settings.TITLE_PREFIX} - Dashboard",
    }
    return render(request, "dashboards.html", context)
