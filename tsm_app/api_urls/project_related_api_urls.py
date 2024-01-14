from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .. import app_tools

api_name_to_project_related_api_model_name = {
    "task": "Task",
    "device": "Device",
    # "team": "Team", need team ?
    "user": "CustomUser",
}

api_model_endpoint_to_view_ptr = {
    "/": (app_tools.get_get_all_models_of_project, 'of'),
    "/filter/": (app_tools.get_filter_models_of_project, 'filter')
}

project_related_api_urlpatterns = [
    path(f"projects/<int:project_id>/{api_name}s{end_point}",
        view=view_ptr(model_name),
        name=f"{api_name}s_{name}_project")
    for end_point, (view_ptr, name) in api_model_endpoint_to_view_ptr.items()
    for api_name, model_name in api_name_to_project_related_api_model_name.items()
]

urlpatterns = format_suffix_patterns(project_related_api_urlpatterns)
