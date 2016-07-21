from rest_framework import serializers
from matricula.models import Alumno, Materia

class Alumno_Serializable(serializers.ModelSerializer):
	class Meta:
		model = Alumno
		fields = ("nombre","apellido","cedula","telefono","correo","direccion")

class Materia_Serializable(serializers.ModelSerializer):
	class Meta:
		model = Materia
		fields = ("nombre","horas","creditos","numcupos","num_Estudiantes")