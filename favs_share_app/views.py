import json

from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http.response import HttpResponse

from CommonClasses.JsonEncoder import *
from CommonClasses.JsonResponser import *

def upload_favs(request):
    context = {}
    return render(
        request,
        'favs_share_app/upload_favs.html',
        context
    )