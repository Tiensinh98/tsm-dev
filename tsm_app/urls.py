from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .api_views import *

urlpatterns = [
    path('', views.index, name='tsm'),
    path('login/', views.login),
    path('tsm-app/', views.tsm_app),
]
api_urlpatterns = [
    path('projects/', view=projects, name='projects'),
    path('projects/<int:pk>/', view=projects),
    path('projects/filter/', view=filter_projects),
    path('projects/add/', view=add_projects),
    path('tasks/', view=tasks, name='tasks'),
    path('tasks/<int:pk>/', view=tasks),
    path('tasks/filter/', view=filter_tasks),
    path('tasks/add/', view=add_tasks),
]
urlpatterns = format_suffix_patterns(urlpatterns + api_urlpatterns)