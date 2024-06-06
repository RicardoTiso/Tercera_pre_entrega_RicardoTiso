from django.shortcuts import render
from django.http import HttpResponse
from AppGymTiso.models import ClasesAlumnos, RegistroInstructores
from .forms import clasesFormulario, registroClasesFormulario
import logging

# Configurar el logger
logger = logging.getLogger(__name__)

# Create your views here.

def inicio(req):
    return render(req, 'inicio.html', {})

def enConstruccion(req):
    return render(req, 'enConstruccion.html', {})

def alumnos(req):
    return render(req, 'alumnos.html', {})

def instructores(req):
    return render(req, 'instructores.html', {})

def mostrar_datos(req):
    datos = RegistroInstructores.objects.all()
    clases = ClasesAlumnos.objects.all()
    return render(req, "mostrar_datos.html", {'datos': datos, 'clases': clases})

def clases(req, nombre, apellido, fechaDeClase, clase):
    nueva_clase=ClasesAlumnos(nombre=nombre, apellido=apellido, fechaDeClase=fechaDeClase, clase=clase)
    nueva_clase.save()
    return render(req, 'clasesForm.html', {})

def lista_clases(req):
    datos = RegistroInstructores.objects.all()
    clases = ClasesAlumnos.objects.all()
    return render(req, "lista_clases.html", {'datos': datos, 'clases': clases})


def registro_clases(req, nombre, apellido, fechaDeClase, clase, titulo, reseña):
    nuevo_registro=RegistroInstructores(
        nombre=nombre, 
        apellido=apellido, 
        fechaDeClase=fechaDeClase, 
        clase=clase, 
        titulo=titulo, 
        reseña=reseña
    )
    nuevo_registro.save()
    return render(req, "registroForm.html", {})

def lista_registro(req):
    datos = RegistroInstructores.objects.all()
    return render(req, "registro_clases.html", {"datos":datos})

def desafios(req):
    return render(req, 'desafios.html', {})

def masPowerNutricion(req):
    return render(req, 'masPower_nutricion.html', {})

def masPowerRutinas(req):
    return render(req, 'masPower_rutinas.html', {})

def masPowerSeguimiento(req):
    return render(req, 'masPower_seguimientoEnLinea.html', {})

def clases_Form(req):
    if req.method == 'POST':
        miFormulario= clasesFormulario(req.POST)

        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            nueva_clase= ClasesAlumnos(nombre=data['nombre'], apellido=data['apellido'], fechaDeClase=data['fechaDeClase'], clase=data['clase'])
            nueva_clase.save()
            return render(req, "inicio_responde.html",{"message":"Alumno registrado con exito."}) 
        else:
            return render(req, "inicio_responde.html", {"message":"Datos invalidos."})     
    else:
        miFormulario= clasesFormulario()
        return render(req, "clasesForm.html",{'miFormulario':miFormulario})
    

def registro_Form(req):
    if req.method == 'POST':
        miFormulario= registroClasesFormulario(req.POST)

        if miFormulario.is_valid():
            data=miFormulario.cleaned_data
            nueva_clase= RegistroInstructores(
                nombre=data['nombre'], 
                apellido=data['apellido'], 
                fechaDeClase=data['fechaDeClase'], 
                clase=data['clase'],
                titulo=data['titulo'], 
                reseña=data['reseña']
            )
            nueva_clase.save()
            return render(req, "inicio_responde.html",{"message":"Curso REGISTRADO con exito, gracias profesor."}) 
        else:
            return render(req, "inicio_responde.html", {"message":"Datos invalidos."})     
    else:
        miFormulario= registroClasesFormulario()
        return render(req, "registroForm.html",{'miFormulario':miFormulario})