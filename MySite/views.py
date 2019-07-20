import json

from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from MySite.settings.base import *
from CommonClasses.JsonEncoder import *
from CommonClasses.JsonResponser import *
from CommonClasses.RequestOperator import *

# TemplateView
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"
    login_url = LOGIN_URL
    redirect_field_name = "redirect_to"

    def get(self, request, **kwargs):
        redirect_to = RequestOperator.get_redirect_to(request)

        context = {}
        if redirect_to is None or "/" == redirect_to:
            return self.render_to_response(context)
        else:
            return HttpResponseRedirect(redirect_to)

"""
---- TemplateView

"""