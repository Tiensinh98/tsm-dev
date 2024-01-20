import typing as tp
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .. import database
from . import view_utils

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
                leader_of_project = database.Project.objects.get(id=project_id).leader
                assignee_json_values = get_all_assignee_json_values_from_project(project_id)
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
        query_params = request.query_params.dict()
        model_class = getattr(database, model_str)
        if model_class == database.CustomUser:
            leader_json = None
            projects = (database.Project.objects
                                 .select_related("leader")
                                 .filter(issue_ptr_id=project_id, leader__isnull=False,
                                         **view_utils.get_related_query_params(query_params, "leader")))
            if len(projects):
                project = projects[0]
                if project.leader is not None:
                    leader_json = project.leader.get_json_value()
            assignee_json_values = get_all_assignee_json_values_from_project(project_id, query_params)
            data = {
                "leader": leader_json,
                "assignees": assignee_json_values
            }
            safe = True
        else:
            if model_class == database.Device:
                queries = model_class.objects.filter(project=project_id, **query_params).order_by('id')
                safe = True
            else:
                queries = model_class.objects.filter(line_project=project_id, **query_params).order_by('id')
            data = [query.get_json_value() for query in queries]
            safe = False
        return JsonResponse(data, status=200, safe=safe)

    return filter_model_of_project


def get_delete_models_of_project(model_str):
    """
    This function acts as a wrapper that returns the filter project-related models
    api respective to the model type
    """
    @api_view(['DELETE'])
    @permission_classes([IsAuthenticated])
    def delete_models_of_project(request, project_id, item_id) -> tp.Union[None, JsonResponse]:
        model_class = getattr(database, model_str)
        if model_class == database.CustomUser:
            # search all tasks in project and set assignee to null
            try:
                user = database.CustomUser.objects.get(id=item_id)
            except Exception as e:
                return JsonResponse({"error": "Can not find user"})
            try:
                project = database.Project.objects.get(id=project_id)
            except Exception as e:
                return JsonResponse({"error": "Can not find project"})
            leader = project.leader
            if leader is not None:
                leader_id = leader.id
                if leader_id == item_id:
                    project.leader = None
            involved_tasks = project.task_set.select_related('assignee').filter(assignee__id=item_id)
            for task in involved_tasks:
                task.assignee = None
                task.save()
            project.save()
            return JsonResponse({"success": "Update all things related to user successfully"}, status=200)
        elif model_class == database.Device:
            try:
                device = database.Device.objects.get(id=item_id)
            except Exception as e:
                return JsonResponse({"error": "Can not find device"})
            try:
                project = database.Project.objects.get(id=project_id)
            except Exception as e:
                return JsonResponse({"error": "Can not find project"})
            if device.project == project:
                device.project = None
                device.save()
            return JsonResponse({"success": "Delete Project of device successfully"}, status=200)

    return delete_models_of_project

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def add_device_to_project(request, project_id, device_id) -> tp.Union[None, JsonResponse]:
    try:
        device = database.Device.objects.get(id=device_id)
    except Exception as e:
        return JsonResponse({"error": "Can not find device"})
    try:
        project = database.Project.objects.get(id=project_id)
    except Exception as e:
        return JsonResponse({"error": "Can not find project"})
    device.project = project
    device.save()
    return JsonResponse({"message": "Add device to project successfully"}, status=200)


def get_all_assignee_json_values_from_project(project_id: int, query_params=None):
    query_params = view_utils.get_related_query_params(query_params, "assignee")
    tasks_of_project = ((database.Task.objects
                        .select_related("line_project", "assignee")
                        .filter(line_project=project_id, assignee__isnull=False, **query_params))
                        .order_by('assignee__id'))
    assignee_json_values = [task.assignee.get_json_value() for task in tasks_of_project]
    return assignee_json_values
