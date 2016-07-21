from django import forms
from .models import Alumno, Materia

class Form_Crear(forms.ModelForm):
	class Meta:
		model = Alumno
		fields = ["nombre","apellido","cedula","telefono","correo","direccion"]

class Form_Materia(forms.ModelForm):
	class Meta:
		model = Materia
		fields = ["nombre","horas","creditos","numcupos","num_Estudiantes"]

class Form_Modificar_A(forms.ModelForm):
	class Meta:
		model = Alumno
		fields = ["nombre","apellido","cedula","telefono","correo","direccion"]

class Form_Modificar_M(forms.ModelForm):
	class Meta:
		model = Materia
		fields = ["nombre","horas","creditos","numcupos","num_Estudiantes"]


#class Form_Modificar(forms.ModelForm):
#	class Meta:
#		model = Alumno
#		fields = ["nombre","apellido","cedula","telefono","correo","direccion"]
