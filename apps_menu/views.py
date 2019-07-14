import json

from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http.response import HttpResponse

from CommonClasses.JsonEncoder import *
from CommonClasses.JsonResponser import *

def main_menu(request):
    context = {}
    return render(
        request,
        'apps_menu/main_menu.html',
        context
    )