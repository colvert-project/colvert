"""
Colvert - The Detection Use Case Management Tool
Copyright (C) 2024  The Colvert Contributors (see README.md / colvert/settings.py)

Licensed under the EUPL, Version 1.2 only (the "Licence");
You may not use this work except in compliance with the Licence.
You may obtain a copy of the Licence, available in the 23 official
languages of the European Union, at:
https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.conf import settings

title_prefix = getattr(settings, "APP_SHORT_NAME")
if getattr(settings, "DEBUG"):
	title_prefix = getattr(settings, "STR_DEBUG") + " - " + title_prefix

# Global placeholders for templates based on 'base.html'
base_context = {
	"pl_lang":				'en', #TODO Get l10n language
	"pl_charset":			'utf-8', #TODO Get settings charset
	"pl_description":		getattr(settings, "APP_SHORT_NAME") + ' - ' + getattr(settings, "APP_DESC"),
	#TODO Review full copyright display and others
	"pl_contributors":		'contrib',
	"pl_licence":			'EUPL-1.2',
    "pl_help":				'URL to issues',
	"pl_powered_by":		'PB',
}
#TODO Retake all the available consts

# Placeholders for templates based on 'app.html', which extends 'base.html'
app_context = {
	"pl_app_company":		'company' #TODO settings.app['company'],
}
app_context.update(base_context)

#TODO basic admin/admin access to review with full login management
def valid_credentials(username: str, password: str) -> bool:
	if (username == 'admin' and password == 'admin'):
		return True
	return False
def signin(request):
	page_name = 'Sign In'

	signin_msg = None
	if request.method == 'POST':
		#TODO manage properly login
		if valid_credentials(escape(request.form.get('username')), escape(request.form.get('password'))):
			#TODO manage properly login
			return redirect('dashboards')
		else:
			#TODO manage properly error messages
			signin_msg = "Invalid credentials."
	
	signin_context = {
		"pl_title":				title_prefix + ' - ' + page_name,
		"pl_signin_base_route":	'signin',
		"pl_signin_msg":		signin_msg,
		"pl_signin_short_name":	getattr(settings, "APP_SHORT_NAME"),
		"pl_signin_footer":		getattr(settings, "APP_COPYRIGHT_HTML") #TODO to manage in base.html
	}
	signin_context.update(app_context)
	
	template = loader.get_template('signin.html')
	return HttpResponse(template.render(signin_context))

def signout(request):
	#TODO Kill session
    return HttpResponse("Hello world!")

def dashboards(request):
    #return HttpResponse("Hello world!")
    template = loader.get_template('dashboards.html')
    return HttpResponse(template.render())
