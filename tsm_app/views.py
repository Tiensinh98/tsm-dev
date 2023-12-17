from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})

def tsm_app(request):
    return render(request, 'index.html', {})

def login(request):
    return render(request, 'index.html', {})
