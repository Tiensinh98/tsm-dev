from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout as lg


def index(request):
    return render(request, 'index.html', {})

def login(request):
    if request.user.is_authenticated:
        return redirect("/tsm-app")
    return render(request, 'index.html', {})

def logout(request):
    lg(request)
    return render(request, 'index.html', {})

def tsm_app(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    return render(request, 'index.html', {})

def tsm_app_projects(request):
    return render(request, 'index.html', {})

def tsm_app_project(request, pk):
    return render(request, 'index.html', {})

def tsm_app_tasks(request):
    return render(request, 'index.html', {})

def tsm_app_task(request, pk):
    return render(request, 'index.html', {})

def tsm_app_devices(request):
    return render(request, 'index.html', {})

def tsm_app_device(request, pk):
    return render(request, 'index.html', {})

def tsm_app_teams(request):
    return render(request, 'index.html', {})

def tsm_app_team(request, pk):
    return render(request, 'index.html', {})

def tsm_app_people(request):
    return render(request, 'index.html', {})

def tsm_app_person(request, pk):
    return render(request, 'index.html', {})