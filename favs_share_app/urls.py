from django.urls import path
from . import views

app_name = 'favs_share_app'

urlpatterns = [
    path('', views.upload_favs, name='upload_favs'),
]