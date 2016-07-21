from django.contrib import admin
from .models import Alumno, Materia
# Register your models here.

class Adm_Alumno(admin.ModelAdmin):
	list_display = ["__str__","nombre"]
	class Meta:
		model = Materia
admin.site.register(Materia,Adm_Alumno)