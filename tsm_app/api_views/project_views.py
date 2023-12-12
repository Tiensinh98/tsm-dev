from django.http import JsonResponse
from rest_framework.decorators import api_view
import datetime
import copy

from . import view_utils
from .. import models


@api_view(['GET', 'DELETE', 'PATCH'])
def projects(request, *args, **kwargs) -> JsonResponse:
    method = request.method
    if method == view_utils.RequestMethod.GET:
        status = 200
        data = {}
        if not len(kwargs):
            all_projects = models.Project.objects.all()
            data = view_utils.filter_query([project.__dict__ for project in all_projects])
        else:
            project_id = kwargs.get('pk', None)
            if project_id is not None:
                try:
                    query = models.Project.objects.filter(baseissue_ptr_id=project_id)
                    if len(query) > 0:
                        data = view_utils.filter_query(query[0].__dict__)
                except models.Project.DoesNotExist as e:
                    return JsonResponse({'message': 'Project not found'}, status=404)

        return JsonResponse(data, status=status, safe=False)
    elif method == view_utils.RequestMethod.DELETE:
        if len(kwargs):
            project_id = kwargs.get('pk', None)
            if project_id is not None:
                try:
                    project = models.Project.objects.get(baseissue_ptr_id=project_id)
                    project.delete()
                    return JsonResponse({'message': 'Delete project successfully'})
                except models.Project.DoesNotExist as e:
                    return JsonResponse({'message': 'Project not found'}, status=404)

            return JsonResponse({'message': 'Project not found'}, status=404)
    else:
        if len(kwargs):
            project_id = kwargs.get('pk', None)
            if project_id is not None:
                try:
                    project = models.Project.objects.get(baseissue_ptr_id=project_id)
                    for field, parameter in request.data.items():
                        setattr(project, field, parameter)
                    project.save()
                except models.Project.DoesNotExist as e:
                    return JsonResponse({'message': 'Project not found'}, status=404)
                query = models.Project.objects.filter(baseissue_ptr_id=project_id)
                if len(query) > 0:
                    data = view_utils.filter_query(query[0].__dict__)
                    return JsonResponse(data)

            return JsonResponse({'message': 'Project not found'}, status=404)


@api_view(['GET'])
def filter_projects(request, *args, **kwargs) -> JsonResponse:
    status = 200
    query_params = request.query_params
    queries = models.Project.objects.filter(**query_params.dict())
    data = [query.get_json_value() for query in queries]
    return JsonResponse(data, status=status, safe=False)


@api_view(['POST'])
def add_projects(request, *args, **kwargs) -> JsonResponse:
    input_data = copy.deepcopy(request.data)
    for key, value in input_data.items():
        if key in {'start_date', 'due_date'}:
            input_data[key] = datetime.datetime.strptime(value, '%Y-%m-%d')
    project_leader_id = input_data.get('project_leader', None)
    if project_leader_id is not None:
        leader = models.Leader.objects.get(baseworker_ptr_id=project_leader_id)
        input_data['project_leader'] = leader
    new_project = models.Project(**input_data.dict())
    new_project.save()
    return JsonResponse({'message': 'Create project successfully'}, status=201)


