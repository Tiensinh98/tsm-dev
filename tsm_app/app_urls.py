from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from tsm_app import views

urlpatterns = [
    path('', views.tsm_app),
    path('projects/', views.tsm_app_projects),
]

urlpatterns = format_suffix_patterns(urlpatterns)
