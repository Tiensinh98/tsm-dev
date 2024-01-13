from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .. import app_tools


api_urlpatterns = [
    path("users/", view=app_tools.get_get_all_models("CustomUser"), name="api_users"),
    path("users/<int:pk>/", view=app_tools.get_get_or_patch_or_delete_model("CustomUser"), name="api_user_one"),
]

urlpatterns = format_suffix_patterns(api_urlpatterns)
