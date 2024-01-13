from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    return render(request, 'index.html', {})

def login(request):
    return render(request, 'index.html', {})

def logout(request):
    return render(request, 'index.html', {})

def tsm_app(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    return render(request, 'index.html', {})

def tsm_app_projects(request):
    return render(request, 'index.html', {})

def tsm_app_tasks(request):
    return render(request, 'index.html', {})

def tsm_app_devices(request):
    return render(request, 'index.html', {})

def tsm_app_teams(request):
    return render(request, 'index.html', {})

def tsm_app_people(request):
    return render(request, 'index.html', {})