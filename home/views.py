

from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template, loader
import random
from home.models import Persona
from home.models import Nproducto
from django.shortcuts import render 


def hola(request):
    return HttpResponse ('hola')


def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse (f'La fecha y hora actual es  {fecha_actual}')



#MANDAR A UNA PÁGINA WEB 

def mi_template(request):
    #cargar_archivo = open (r'C:\Users\ck_ka\OneDrive\Documentos\ProyectoFinal\proyectoGit\templates\template.html', 'r')
    #template = Template (cargar_archivo.read())
    #cargar_archivo.close()
    #contexto = Context()
    #template_renderizado = template.render(contexto)
    templete = loader.get_template ('home/template.html')
    templete_renderizado = templete.render()
    return HttpResponse (templete_renderizado)



def crear_persona(request, nombre, apellido):
    persona = Persona(nombre=nombre, apellido=apellido, edad=random.randrange(1,99), fecha_nacimiento=datetime.now())
    persona.save()
    return render (request, 'home/crear_persona.html', {'persona': persona})

#def crear_persona(request):
#    templete = loader.get_template ('crear_persona.html')
#    templete_renderizado = templete.render(templete_renderizado)
#    return HttpResponse (templete_renderizado)


#def ver_personas(request):
#   personas =  Persona.objects.all()
#   templete = loader.get_template ('ver_personas.html')
#   templete_renderizado = templete.render({'personas': personas})
#   return HttpResponse (templete_renderizado)



def ver_personas(request):
   personas =  Persona.objects.all()
   return render (request, 'home/ver_personas.html', {'personas': personas})




def index(request):
    return render (request, 'home/index.html')



def productos(request):
    return render (request, 'home/productos.html')


def abautus(request):
    return render (request, 'home/abautus.html')


def login(request):
    return render (request, 'home/login.html')


def admon_productos(request):
    return render (request, 'home/admon_productos.html')


def crear_productos(request):
    return render (request, 'home/crear_productos.html')


def crear_productos(request):
    #persona = Persona(nombre=nombre, apellido=apellido, edad=random.randrange(1,99), fecha_nacimiento=datetime.now())
    #persona.save()
    print('POST')
    print(request.POST)
    prenda = request.POST.get('prenda')
    material = request.POST.get('material')
    costo = request.POST.get('costo')
    existencia = request.POST.get('existencia')
    producto = Nproducto(prenda=prenda, material=material, costo=costo, existencia=existencia)
    producto.save()
    return render (request, 'home/crear_productos.html', {})