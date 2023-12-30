import typing as tp
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from . import view_utils as vu
from .. import database


def get_get_all_models(model_str):
    """
    This function acts as a wrapper that returns the get models
    api respective to the model type
    """

    @api_view(['GET'])
    def get_all_models(request) -> tp.Union[None, JsonResponse]:
        """
        This GET API is used to get all current models
        e.g. for Project
        Required:
            None

        Optional:
            end_date: datetime - end date of project
            ...
        Returns:
            JsonResponse
        """
        all_models = (getattr(database, model_str).objects
                      .all().exclude(name__startswith='dummy').order_by('id'))
        data = [model.get_json_value() for model in all_models]
        return JsonResponse(data, status=200, safe=False)

    return get_all_models


def get_get_or_patch_or_delete_model(model_str):
    """
    This function acts as a wrapper that return the get/patch/delete a specified model api
    """
    model_class = getattr(database, model_str)

    @api_view(['GET', 'DELETE', 'PATCH'])
    def get_or_patch_or_delete_project(request, *args, **kwargs) -> tp.Union[None, JsonResponse]:
        """
        This GET/DELETE/PATCH API is used to get/delete/modify and specified model
        Specifically, for PATCH API, user can provide modify data to update the model
        e.g. for Project
        Required:
            baseissue_ptr_id: int - the project id

        Optional:
            end_date: datetime - end date of project
            ...
        Returns:
            JsonResponse
        """
        method = request.method
        model_id = kwargs.get('pk', None)
        if model_id is not None:
            if model_class.__base__ != object:
                key = model_class.__base__.__name__.lower() + '_ptr_id'
            else:
                key = 'id'
            filterer = {key: model_id}
            if method == vu.RequestMethod.GET:
                data = {}
                try:
                    model = getattr(database, model_str).objects.get(**filterer)
                    data = model.get_json_value()
                except model_class.DoesNotExist:
                    return JsonResponse({'message': f'{model_str} not found'}, status=404)
                return JsonResponse(data, status=200, safe=False)
            elif method == vu.RequestMethod.DELETE:
                try:
                    model = getattr(database, model_str).objects.get(**filterer)
                    model.delete()
                except model_class.DoesNotExist:
                    return JsonResponse({'message': f'Can not delete {model_str}'}, status=404)
                return JsonResponse({'message': f'Delete {model_str} successfully'})
            else:
                try:
                    field_to_converter = model_class.get_non_primitive_field_to_converter()
                    model = model_class.objects.get(**filterer)
                    for field, parameter in request.data.items():
                        converter = field_to_converter.get(field, None)
                        if converter is None:
                            value = parameter
                        else:
                            value = converter(parameter)
                            if isinstance(value, tuple):
                                value = value[0]
                        setattr(model, field, value)
                    model.save()
                except model_class.DoesNotExist as e:
                    return JsonResponse({'message': f'{model_str} not found'}, status=404)
                model = model_class.objects.get(**filterer)
                return JsonResponse(model.get_json_value())
        return JsonResponse({'message': 'Wrong route'}, status=404)
    return get_or_patch_or_delete_project


def get_filter_models(model_str):
    """
    This function acts as a wrapper that returns the filter models
    api respective to the model type
    """

    @api_view(['GET'])
    def filter_models(request) -> JsonResponse:
        """
        This GET API is used to filter through all models that match a couple
        of criterion
        e.g. for Project
        Required:
            None

        Optional:
            end_date: datetime - end date of project
            ...
        Returns:
            JsonResponse
        """
        query_params = request.query_params
        queries = (getattr(database, model_str)
                   .objects.filter(**query_params.dict()).order_by('id'))
        data = [query.get_json_value() for query in queries]
        return JsonResponse(data, status=200, safe=False)

    return filter_models


def get_create_model(model_str):
    """
    This function acts as a wrapper that returns the create model
    api respective to the model type
    """
    field_to_converter = getattr(database, model_str).get_non_primitive_field_to_converter()

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def create_model(request) -> JsonResponse:
        """
        This POST API is used to create a new Model with some fields
        e.g. for Project model
        Required:
            issue_name: str - name of project

        Optional:
            project_leader: Leader - leader of project
            start_date: datetime - start date of project
            ...

        Returns:
            JsonResponse
        """
        data = {}
        for key, value in request.data.items():
            converter = field_to_converter.get(key)
            if converter is not None:
                # modify the key back to the original name to create object properly
                value = converter(value)
                if isinstance(value, tuple):
                    value, key = value
                data[key] = value
            else:
                data[key] = value
        new_model = getattr(database, model_str)(**data)
        new_model.save()
        return JsonResponse({'message': f'Create {model_str} successfully'}, status=201)

    return create_model
