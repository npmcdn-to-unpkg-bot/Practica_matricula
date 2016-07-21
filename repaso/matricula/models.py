from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Alumno(models.Model):

	nombre = models.CharField(max_length=30)
 	apellido = models.CharField(max_length=30)
 	cedula = models.CharField(max_length=30)
 	telefono = models.CharField(max_length=30)
 	correo = models.EmailField(max_length=30,blank=True,null=True)
 	direccion = models.TextField(max_length=10,default="direccion")	

 	def __str__(self):
 		return str(self.cedula)

class Materia(models.Model):

	nombre = models.CharField(max_length=30)
 	horas = models.CharField(max_length=20)
 	creditos = models.CharField(max_length=20)
 	numcupos = models.CharField(max_length=20)
 	num_Estudiantes = models.CharField(max_length=10)
 	
 	def __str__(self):
 		return str(self.nombre)




 	