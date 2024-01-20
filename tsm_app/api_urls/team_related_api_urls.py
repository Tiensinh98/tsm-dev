from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .. import app_tools


api_model_endpoint_to_view_ptr = {
    "/": (app_tools.get_get_all_models_of_project, 'of'),
    "/filter/": (app_tools.get_filter_models_of_project, 'filter')
}

team_related_api_urlpatterns = [
    path("teams/<int:team_id>/people/",
         view=app_tools.get_team_people, name="people_of_team"),
    path("teams/<int:team_id>/people/filter/",
         view=app_tools.filter_team_people, name="filter_people_of_team"),
    path("teams/<int:team_id>/people/<int:member_id>/",
         view=app_tools.remove_people_of_team, name="remove_people_of_team"),
    path("teams/<int:team_id>/people/add-leader/<int:member_id>/",
             view=app_tools.add_team_leader, name="add_team_leader"),
    path("teams/<int:team_id>/people/add-member/<int:member_id>/",
                 view=app_tools.add_team_member, name="add_member_to_team"),
]

urlpatterns = format_suffix_patterns(team_related_api_urlpatterns)
