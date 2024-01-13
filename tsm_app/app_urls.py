from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from tsm_app import views

urlpatterns = [
    path('', views.tsm_app),
    path('projects/', views.tsm_app_projects),
    path('projects/<int:pk>/', views.tsm_app_project),
    path('tasks/', views.tsm_app_tasks),
    path('tasks/<int:pk>/', views.tsm_app_task),
    path('devices/', views.tsm_app_devices),
    path('devices/<int:pk>/', views.tsm_app_device),
    path('teams/', views.tsm_app_teams),
    path('teams/<int:pk>/', views.tsm_app_team),
    path('people/', views.tsm_app_people), # /tsm-app/people/
    path('people/<int:pk>/', views.tsm_app_person),
]

urlpatterns = format_suffix_patterns(urlpatterns)
