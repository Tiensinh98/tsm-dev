from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .. import app_tools

api_name_to_model_name = {
    "project": "Project",
    "task": "Task",
    "device": "Device",
    "team": "Team",
    "user": "CustomUser"
}
api_model_endpoint_to_view_ptr = {
    "/": (app_tools.get_get_all_models, ''),
    "/<int:pk>/": (app_tools.get_get_or_patch_or_delete_model, 'one'),
    "/filter/": (app_tools.get_filter_models, 'filter'),
    "/add/": (app_tools.get_create_model, 'add')
}
api_urlpatterns = [
    path(f'{api_name}s{endpoint}', view=view_ptr(model_name), name=f'{api_name}s{name}')
    for endpoint, (view_ptr, name) in api_model_endpoint_to_view_ptr.items()
    for api_name, model_name in api_name_to_model_name.items()
]

urlpatterns = format_suffix_patterns(api_urlpatterns)

