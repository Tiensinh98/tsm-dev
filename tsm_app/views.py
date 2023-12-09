from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import generic, View
from . models import Project


def index(request):
    return render(request, 'index.html', {})

def task(request):
    data = {
        'key1': 'value1',
        'key2': 'value2',
    }

    # Create a JsonResponse instance with your data
    response = JsonResponse(data, status=200)
    print('Response: ', response)
    return response


class ProjectView(View):

    @classmethod
    def get(cls, request, *args, **kwargs):
        if len(kwargs):
            project_id = kwargs.get('pk', None)
            if project_id is None:
                return JsonResponse([], status=200)
            project = Project.objects.get(baseissue_ptr_id=int(project_id))
            return JsonResponse(project.__dict__, status=200)
        try:
            data = [project.__dict__ for project in Project.objects.all()]
            # remove unused keys i.e. _state, id, ptr_id
            status = 200
        except Exception as e:
            data = []
            status = 404
        return JsonResponse(data, status=status)