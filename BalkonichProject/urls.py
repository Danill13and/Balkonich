"""
URL configuration for BalkonichProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from . import settings
from BalkonichApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('insulation/', views.insulation, name='insulation'),
    path('electrical_installation/', views.electrical_installation, name='electrical_installation'),
    path('interior_decoration/', views.interior_decoration, name='interior_decoration'),
    path('slopes/', views.slopes, name='slopes'),
    path('armored_film/', views.armored_film, name='armored_film')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
