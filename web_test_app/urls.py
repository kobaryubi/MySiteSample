from django.urls import path
from . import views
from .views import *

app_name = 'web_test_app'

urlpatterns = [
    path('', FrontSamplesView.as_view(), name='front_samples'),
    path('bootstrap_samples', BootstrapSamplesView.as_view(), name='bootstrap_samples'),

    # template samples
    path('sample_template_view', SampleTemplateView.as_view(), name='sample_template_view'),
]
