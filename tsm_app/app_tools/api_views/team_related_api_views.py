import typing as tp
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .. import database
from . import view_utils

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_team_people(request, team_id) -> tp.Union[None, JsonResponse]:
    """
    This view is used to get the team leader information
    """
    try:
        team = database.Team.objects.get(id=team_id)
    except Exception as e:
        return JsonResponse({"error": "Could not find team"}, status=404)
    leader_json = None
    leader = team.leader
    if leader is not None:
        leader_json = leader.get_json_value()
    members = team.members.all()
    ret = {"leader": leader_json, "members": [member.get_json_value() for member in members]}
    return JsonResponse(ret, status=200, safe=True)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def filter_team_people(request, team_id) -> tp.Union[None, JsonResponse]:
    query_params = request.query_params.dict()
    try:
        team = database.Team.objects.get(id=team_id)
    except Exception as e:
        return JsonResponse({"error": "Could not find team"}, status=404)
    leader = team.leader
    leader_json = None
    if leader is not None:
        teams = database.Team.objects.filter(
            id=team_id, **view_utils.get_related_query_params(query_params, 'leader'))
        if len(teams):
            leader_json = teams[0].leader.get_json_value()
    queries = database.CustomUser.objects.filter(team=team_id, **query_params).order_by('id')
    members = [query.get_json_value() for query in queries]
    return JsonResponse({"leader": leader_json, "members": members}, status=200, safe=False)


