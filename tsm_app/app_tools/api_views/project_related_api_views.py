import typing as tp
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .. import database

def get_get_all_models_of_project(model_str):
    """
    This function acts as a wrapper that returns the get project-related models
    api respective to the model type
    """

    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def get_all_models_of_project(request, project_id) -> tp.Union[None, JsonResponse]:
        model_class = getattr(database, model_str)
        if model_class == database.CustomUser:
            try:
                # TODO: query by multiple keys from multiple tables
                leader_of_project = database.Project.objects.get(id=project_id).leader
                tasks_of_project = database.Task.objects.filter(line_project=project_id)
                assignee_json_values = [assignee.get_json_value()
                                        for task in tasks_of_project
                                        if (assignee:= task.assignee) is not None]
                data = {
                    "leader": leader_of_project.get_json_value() if leader_of_project is not None else None,
                    "assignees": assignee_json_values
                }
                safe = True
            except Exception as e:
                return JsonResponse([], status=404)
        else:
            if model_class == database.Device:
                queries = model_class.objects.filter(project=project_id).order_by('id')
            else:
                queries = model_class.objects.filter(line_project=project_id).order_by('id')
            data = [query.get_json_value() for query in queries]
            safe = False
        return JsonResponse(data, status=200, safe=safe)

    return get_all_models_of_project

def get_filter_models_of_project(model_str):
    """
    This function acts as a wrapper that returns the filter project-related models
    api respective to the model type
    """
    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def filter_model_of_project(request, project_id) -> tp.Union[None, JsonResponse]:
        model_class = getattr(database, model_str)
        query_params = request.query_params
        queries = (getattr(database, model_str)
                   .objects.filter(**query_params.dict(), line_project=project_id).order_by('id'))
        data = [query.get_json_value() for query in queries]
        return JsonResponse(data, status=200, safe=False)

    return filter_model_of_project
