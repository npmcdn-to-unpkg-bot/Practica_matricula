from django.shortcuts import render
from matricula.models import Alumno, Materia
from rest_framework import  viewsets
from .serializable import Alumno_Serializable, Materia_Serializable

# Create your views here.
class Alumno_viewSet(viewsets.ModelViewSet):
	serializer_class = Alumno_Serializable
	queryset = Alumno.objects.all().order_by('apellido')

class Materia_viewSet(viewsets.ModelViewSet):
	serializer_class = Materia_Serializable
	queryset = Materia.objects.filter(numcupos__lte=29)