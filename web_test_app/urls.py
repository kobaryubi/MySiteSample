from django.urls import path
from . import views
from .views import SampleTemplateView

app_name = 'web_test_app'

urlpatterns = [
    path('', views.front_samples, name='front_samples'),
    path('bootstrap_samples', views.bootstrap_samples, name='bootstrap_samples'),

    # template samples
    path('sample_template_view', SampleTemplateView.as_view(), name='sample_template_view'),
]
