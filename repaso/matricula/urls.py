from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [     
	url(r'^$','matricula.views.listar'),
	url(r'^crear_alumno/$','matricula.views.crear_alumno'),
	url(r'^crear_materias/$','matricula.views.crear_materias'),
	url(r'^eliminar_alumno/$','matricula.views.eliminar_alumno'),
	url(r'^confirmacion_eliminar/$','matricula.views.confirmacion_eliminar'),
	url(r'^modificar_alumno/$','matricula.views.modificar_alumno'),
	url(r'^eliminar_materia/$','matricula.views.eliminar_materia'),
	url(r'^confirmacion_eliminar_materia/$','matricula.views.confirmacion_eliminar_materia'),
	url(r'^modificar_materia/$','matricula.views.modificar_materia'),

]
