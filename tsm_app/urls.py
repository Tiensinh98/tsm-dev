from django.urls import path
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'tsm_app'

urlpatterns = [
    path('', views.index)
]

urlpatterns = format_suffix_patterns(urlpatterns)
