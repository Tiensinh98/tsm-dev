from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})

def login(request):
    return render(request, 'index.html', {})

def home(request):
    return render(request, 'index.html', {})

def logout(request):
    return render(request, 'index.html', {})

def tsm_app(request):
    # redirect when user is logged out
    return render(request, 'index.html', {})

def tsm_app_projects(request):
    return render(request, 'index.html', {})
