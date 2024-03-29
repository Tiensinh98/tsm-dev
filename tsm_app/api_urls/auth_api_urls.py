from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .. import app_tools

urlpatterns = [
    path('login/', app_tools.login, name='api_login'),
    path('logout/', app_tools.logout, name='api_logout'),
    path('register/', app_tools.register), # <int:year>/<int:month>/<int:day>/<slug:post>/
    path('csrf-token/', app_tools.get_csrf_token, name='csrf_token'),
    path('password-change/', app_tools.password_change, name='api_password_change')
]
urlpatterns = format_suffix_patterns(urlpatterns)


