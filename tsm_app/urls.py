from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from . import app_tools

urlpatterns = [
    path('', views.index),
    path('login/', app_tools.login, name='login'),
    path('logout/', app_tools.logout, name='logout'),
    path('register/', app_tools.register),
    path('tsm-app/', views.tsm_app), # <int:year>/<int:month>/<int:day>/<slug:post>/
]

api_model_names = ['project', 'task']
api_model_endpoint_to_view_ptr = {
    "/": (app_tools.get_get_all_models, ''),
    "/<int:pk>/": (app_tools.get_get_or_patch_or_delete_model, 'one'),
    "/filter/": (app_tools.get_filter_models, 'filter'),
    "/add/": (app_tools.get_create_model, 'add'),
}
api_urlpatterns = [
    path(f'{model_name}s{endpoint}', view=view_ptr(model_name.capitalize()), name=f'{model_name}s{name}')
    for endpoint, (view_ptr, name) in api_model_endpoint_to_view_ptr.items()
    for model_name in api_model_names
]

urlpatterns = format_suffix_patterns(urlpatterns + api_urlpatterns)
