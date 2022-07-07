from django.shortcuts import render, redirect

# Cuando ingresemos a la vista "home" tenemos que listar
# todos nuestros cursos, para ello se utiliza el ORM
# para poder hacer todas las interacciones con la base
# de datos, en este caso el modelo es "Curso"
from .models import Curso
from django.contrib import messages


# Create your views here.

def home(request):
    cursos_listados=Curso.objects.all() #nos retorna el listado de todos los cursos
    # messages.success(request,'¡Cursos listados!')
    return render(request,"gestionCursos.html", {"cursos":cursos_listados})

def registrarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']

    curso=Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect('/')

def edicionCurso(request, codigo):
    curso=Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso":curso})

def editarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']

    curso=Curso.objects.get(codigo=codigo)
    curso.nombre=nombre
    curso.creditos=creditos
    curso.save()
    return redirect('/')



def eliminacionCurso(request, codigo):
    curso=Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/')


