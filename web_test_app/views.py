import json

from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http.response import HttpResponse
from django.views.generic import TemplateView

from CommonClasses.JsonEncoder import *
from CommonClasses.JsonResponser import *

def front_samples(request):
    context = {}
    return render(
        request,
        'web_test_app/front_samples.html',
        context
    )

def bootstrap_samples(request):
    context = {}
    return render(
        request,
        'web_test_app/bootstrap_samples.html',
        context
    )

# TemplateView
class SampleTemplateView(TemplateView):
    template_name = "web_test_app/sample_template_view.html"
# ListView