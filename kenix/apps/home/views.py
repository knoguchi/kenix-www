import logging

from django.views.generic import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "home/index.html"

    log = logging
