from django.urls import path
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns

from .. import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('home/', views.home),
    path('logout/', views.logout),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
