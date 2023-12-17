import typing as tp
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as lg, logout as lgt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .. import database

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request) -> tp.Union[None, JsonResponse]:
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        lg(request, user)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})


@api_view(['POST'])
@permission_classes([AllowAny])
def logout(request) -> tp.Union[None, JsonResponse]:
    user = request.user
    if user.is_authenticated:
        lgt(request)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request) -> tp.Union[None, JsonResponse]:
    username = request.data['username']
    password = request.data['password']
    try:
        user = database.CustomUser(username=username, password=password)
        user.set_password(password)
        user.save()
        return JsonResponse({'success': True, 'message': 'Create User successfully'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': e})
