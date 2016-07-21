from django.shortcuts import render,redirect
from .forms import Form_Crear, Form_Materia, Form_Modificar_A, Form_Modificar_M
from .models import Alumno, Materia
from django.contrib import messages
# Create your views here.


def listar(request):
	materia = Materia.objects.all()
	alumno = Alumno.objects.all()
	context = {
		'alumno':alumno,
		'materia':materia,
	}

	return render(request,'listar.html',context)

def crear_alumno(request):
	f = Form_Crear(request.POST or None)
	context ={
		"form":f,
	}

	if f.is_valid():
		datos_form       = f.cleaned_data
		alumno           = Alumno()
		alumno.nombre    = datos_form.get("nombre")
		alumno.apellido  = datos_form.get("apellido")
		alumno.cedula    = datos_form.get("cedula")
		alumno.telefono  = datos_form.get("telefono")
		alumno.correo 	 = datos_form.get("correo")
		alumno.direccion = datos_form.get("direccion")
		alumno.save()

		if(alumno.save() != True):
			messages.add_message(request, messages.ERROR, "No se ha podido crear el Alumno", fail_silently=True)
		else:	
			messages.add_message(request, messages.SUCCESS, "Se ha creado un nuevo Alumno", fail_silently=True)
		return redirect('/matricula')
	context ={
		"form":f,
	}
	return render(request,'crear_alumno.html',context)

def crear_materias(request):
	f = Form_Materia(request.POST or None)
	context = {
		"form":f,
	}

	if f.is_valid():
		datos_form 				= f.cleaned_data
		materia 				= Materia()
		materia.nombre 			= datos_form.get("nombre")
		materia.horas 			= datos_form.get("horas")
		materia.creditos 		= datos_form.get("creditos")
		materia.numcupos 		= datos_form.get("numcupos")
		materia.num_Estudiantes = datos_form.get("num_Estudiantes")
		materia.save()

		if(materia.save() != True):
			messages.add_message(request, messages.ERROR, "No se ha podido crear la Materia", fail_silently=True)
		else:	
			messages.add_message(request, messages.SUCCESS, "Se ha creado una nueva Materia", fail_silently=True)
		return redirect('/matricula')
	context ={
		"form":f,
	}
	return render(request,'crear_materia.html',context)

def eliminar_alumno(request):
	alumno = Alumno.objects.get(cedula=request.GET['cedula'])
	context = {
		'alumno':alumno,
	}
	return render(request,'eliminar_alumno.html',context)

def confirmacion_eliminar(request):
	alumno = Alumno.objects.get(cedula=request.GET['cedula'])
	if (alumno.delete()):
		messages.add_message(request, messages.SUCCESS, "Se ha eliminado el alumno", fail_silently=True)
	else: 
		messages.add_message(request, messages.ERROR, "No se ha eliminado el alumno", fail_silently=True)
	return redirect(listar)

def modificar_alumno(request):
	alumno = Alumno.objects.get(cedula=request.GET['cedula'])
	f = Form_Modificar_A(request.POST or None)
	context = {
		'alumno':alumno,
		'form':f,
	}
	f.fields['nombre'].initial	 = alumno.nombre
	f.fields['apellido'].initial = alumno.apellido
	f.fields['cedula'].initial 	 = alumno.cedula
	f.fields['telefono'].initial = alumno.telefono
	f.fields['correo'].initial 	 = alumno.correo
	f.fields['direccion'].initial= alumno.direccion

	if request.method == 'POST':
		if f.is_valid():
			f_data = f.cleaned_data
			alumno.nombre 	= f_data.get('nombre')
			alumno.apellido = f_data.get('apellido')
			alumno.cedula 	= f_data.get('cedula')
			alumno.telefono = f_data.get('telefono')
			alumno.correo	= f_data.get('correo')
			alumno.direccion= f_data.get('direccion')
			if (alumno.save()):
				messages.add_message(request, messages.ERROR, "No se ha modificado el alumno", fail_silently=True)
			else:	
				messages.add_message(request, messages.SUCCESS, "Se ha modificado el alumno", fail_silently=True)
			return redirect(listar)

	return render(request,'modificar_alumno.html',context)

def eliminar_materia(request):
	materia = Materia.objects.get(nombre=request.GET['nombre'])
	context = {
		'materia':materia,
	}
	return render(request,'eliminar_materia.html',context)

def confirmacion_eliminar_materia(request):
	materia = Materia.objects.get(nombre=request.GET['nombre'])
	if (materia.delete()):
		messages.add_message(request, messages.SUCCESS, "Se ha eliminado la materia", fail_silently=True)
	else: 
		messages.add_message(request, messages.ERROR, "No se ha eliminado la materia", fail_silently=True)
	return redirect(listar)

def modificar_materia(request):
	materia = Materia.objects.get(nombre=request.GET['nombre'])
	f = Form_Modificar_M(request.POST or None)
	context = {
		'materia':materia,
		'form':f,
	}
	f.fields['nombre'].initial	 		= materia.nombre
	f.fields['horas'].initial 			= materia.horas
	f.fields['creditos'].initial 		= materia.creditos
	f.fields['numcupos'].initial 		= materia.numcupos
	f.fields['num_Estudiantes'].initial = materia.num_Estudiantes

	if request.method == 'POST':
		if f.is_valid():
			f_data = f.cleaned_data
			materia.nombre 			= f_data.get('nombre')
			materia.horas 			= f_data.get('horas')
			materia.creditos 		= f_data.get('creditos')
			materia.numcupos 		= f_data.get('numcupos')
			materia.num_Estudiantes	= f_data.get('num_Estudiantes')
			if (materia.save()):
				messages.add_message(request, messages.ERROR, "No se ha modificado el materia", fail_silently=True)
			else:	
				messages.add_message(request, messages.SUCCESS, "Se ha modificado el materia", fail_silently=True)
			return redirect(listar)

	return render(request,'modificar_materia.html',context)

