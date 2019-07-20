import json

from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http.response import HttpResponse
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from MySite.settings.base import *
from CommonClasses.JsonEncoder import *
from CommonClasses.JsonResponser import *

class FrontSamplesView(LoginRequiredMixin, TemplateView):
    template_name = "web_test_app/front_samples.html"
    login_url = LOGIN_URL
    redirect_field_name = REDIRECT_FIELD_NAME

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BootstrapSamplesView(LoginRequiredMixin, TemplateView):
    template_name = "web_test_app/bootstrap_samples.html"
    login_url = LOGIN_URL
    redirect_field_name = REDIRECT_FIELD_NAME

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# TemplateView
class SampleTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "web_test_app/sample_template_view.html"
    login_url = LOGIN_URL
    redirect_field_name = REDIRECT_FIELD_NAME

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["foo"] = "bar"
        return context

# ListView
class SampleListView(LoginRequiredMixin, ListView):
    login_url = LOGIN_URL
    redirect_field_name = REDIRECT_FIELD_NAME

