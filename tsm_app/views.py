from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})

def tsm_app(request):
    return render(request, 'index.html', {})

def login(request):
    return render(request, 'index.html', {})


# @api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
# def projects(request, *args, **kwargs):
#     return JsonResponse({}, status=200)

# @api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
# def tasks(request, *args, **kwargs):
#     return JsonResponse({}, status=200)
#
# @api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
# def leaders(request, *args, **kwargs):
#     return JsonResponse({}, status=200)
#
# @api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
# def workers(request, *args, **kwargs):
#     return JsonResponse({}, status=200)
#
# @api_view(['POST'])
# def login(request, *args, **kwargs):
#     return JsonResponse({}, status=200)
#
# @api_view(['POST'])
# def logout(request, *args, **kwargs):
#     return JsonResponse({}, status=200)
#
# @api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
# def devices(request, *args, **kwargs):
#     return JsonResponse({}, status=200)
#
# @api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
# def user_settings(request, *args, **kwargs):
#     return JsonResponse({}, status=200)
#
# @api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
# def timeline(request, *args, **kwargs):
#     return JsonResponse({}, status=200)
#
# @api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
# def components(request, *args, **kwargs):
#     return JsonResponse({}, status=200)