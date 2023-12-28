import typing as tp
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, views as auth_views
from django.contrib.auth.forms import PasswordResetForm
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from .. import database

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request) -> tp.Union[None, JsonResponse]:
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})


@api_view(['POST'])
@permission_classes([AllowAny])
def logout(request) -> tp.Union[None, JsonResponse]:
    user = request.user
    if user.is_authenticated:
        auth_logout(request)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request) -> tp.Union[None, JsonResponse]:
    username = request.data['username']
    email = request.data['email']
    password = request.data['password']
    try:
        user = database.CustomUser(
            username=username, email=email, password=password)
        user.set_password(password)
        user.save()
        return JsonResponse({'success': True, 'message': 'Create User successfully'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': e})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def password_change(request) -> tp.Union[None, JsonResponse]:
    username = request.data['username']
    new_password = request.data['password']
    try:
        user = database.CustomUser.objects.get(username=username)
        user.set_password(new_password)
        user.save()
        return JsonResponse({'success': True, 'message': 'Change password successfully'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': e})


class CustomPasswordResetView(auth_views.PasswordResetView):
    form_class = PasswordResetForm
    # template_name = 'registration/password_reset_form.html'

    def form_valid(self, form):
        # Check if the email address exists in the database
        email = form.cleaned_data['email']
        if database.CustomUser.objects.filter(email=email).exists():
            return super().form_valid(form)
        else:
            # Add custom logic for handling non-existing email
            return render(self.request, 'registration/non_existing_email.html', context={'email': email})

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)