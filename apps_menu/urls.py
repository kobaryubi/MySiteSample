from django.urls import path
from . import views

app_name = 'apps_menu'

urlpatterns = [
    path('', views.main_menu, name='main_menu'),
]
