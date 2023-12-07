from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse


def index(request):
    print(User.objects)
    return HttpResponse("Hello, world. You're at the polls index.")
