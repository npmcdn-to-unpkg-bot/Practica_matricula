"""repaso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from servicioWeb.views import Alumno_viewSet, Materia_viewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'alumno',Alumno_viewSet)
router.register(r'materia',Materia_viewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
   	url(r'^matricula/', include('matricula.urls')),   
   	url(r'^api/', include(router.urls)), 
]
