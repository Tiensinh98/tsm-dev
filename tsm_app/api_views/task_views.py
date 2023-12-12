from django.http import JsonResponse
from rest_framework.decorators import api_view
import copy
import datetime

from . import view_utils
from .. import models


@api_view(['GET', 'DELETE', 'PATCH'])
def tasks(request, *args, **kwargs) -> JsonResponse:
    method = request.method
    if method == view_utils.RequestMethod.GET:
        status = 200
        data = {}
        if not len(kwargs):
            all_tasks = models.Task.objects.all()
            data = view_utils.filter_query([task.__dict__ for task in all_tasks])
        else:
            task_id = kwargs.get('pk', None)
            if task_id is not None:
                try:
                    query = models.Task.objects.filter(baseissue_ptr_id=task_id)
                    if len(query) > 0:
                        data = view_utils.filter_query(query[0].__dict__)
                except models.Task.DoesNotExist as e:
                    return JsonResponse({'message': 'Task not found'}, status=404)

        return JsonResponse(data, status=status, safe=False)
    elif method == view_utils.RequestMethod.DELETE:
        if len(kwargs):
            task_id = kwargs.get('pk', None)
            if task_id is not None:
                try:
                    task = models.Task.objects.get(baseissue_ptr_id=task_id)
                    task.delete()
                    return JsonResponse({'message': 'Delete task successfully'})
                except models.Task.DoesNotExist as e:
                    return JsonResponse({'message': 'Task not found'}, status=404)

            return JsonResponse({'message': 'Task not found'}, status=404)
    else:
        if len(kwargs):
            task_id = kwargs.get('pk', None)
            if task_id is not None:
                try:
                    task = models.Task.objects.get(baseissue_ptr_id=task_id)
                    for field, parameter in request.data.items():
                        setattr(task, field, parameter)
                    task.save()
                except models.Task.DoesNotExist as e:
                    return JsonResponse({'message': 'Task not found'}, status=404)
                query = models.Task.objects.filter(baseissue_ptr_id=task)
                if len(query) > 0:
                    data = view_utils.filter_query(query[0].__dict__)
                    return JsonResponse(data)

            return JsonResponse({'message': 'Task not found'}, status=404)


@api_view(['GET'])
def filter_tasks(request, *args, **kwargs) -> JsonResponse:
    status = 200
    query_params = request.query_params
    queries = models.Task.objects.filter(**query_params.dict())
    data = [query.get_json_value() for query in queries]
    return JsonResponse(data, status=status, safe=False)


@api_view(['POST'])
def add_tasks(request, *args, **kwargs) -> JsonResponse:
    input_data = copy.deepcopy(request.data)
    for key, value in input_data.items():
        if key in {'start_date', 'due_date'}:
            input_data[key] = datetime.datetime.strptime(value, '%Y-%m-%d')
    worker_id = input_data.get('worker', None)
    project_id = input_data.get('head_project', None)
    if worker_id is not None:
        worker = models.Worker.objects.get(baseworker_ptr_id=worker_id)
        input_data['worker'] = worker
    if project_id is not None:
        project = models.Project.objects.get(baseissue_ptr_id=project_id)
        input_data['head_project'] = project
    new_task = models.Task(**input_data.dict())
    new_task.save()
    return JsonResponse({'message': 'Create task successfully'}, status=201)
