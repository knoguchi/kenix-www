import logging

from django.views.generic import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from kenix.settings import CLIENT_SECRETS
from django.views.generic import TemplateView
from django.shortcuts import render_to_response

import json
with open(CLIENT_SECRETS) as f:
    secrets = json.load(f)

class HomeView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['CLIENT_ID'] = secrets['web']['client_id']
        context['SCOPES'] = "https://www.googleapis.com/auth/userinfo.email"
        return context
