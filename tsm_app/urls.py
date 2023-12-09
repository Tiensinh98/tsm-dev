from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='tsm'),
    path('task/', views.task, name='task'),
    path('projects/', views.ProjectView.as_view(), name='projects'),
    path('projects/<int:pk>/', view=views.ProjectView.as_view(), name='project'),
]