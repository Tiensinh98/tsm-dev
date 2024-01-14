"""tsm_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
from django.conf import settings

urlpatterns = [
    path("", include("tsm_app.urls")),
    path("user/", include("tsm_app.user_urls")),
    path("tsm-app/", include("tsm_app.app_urls")),
    path("api/", include("tsm_app.api_urls.auth_api_urls")),
    path("api/", include("tsm_app.api_urls.basic_model_api_urls")),
    path("api/", include("tsm_app.api_urls.project_related_api_urls")),
    path("admin/", admin.site.urls)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
