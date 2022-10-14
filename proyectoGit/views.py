

from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template, loader
import random

from home.models import Persona


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
    templete = loader.get_template ('template.html')
    templete_renderizado = templete.render()
    return HttpResponse (templete_renderizado)



def crear_persona(request, nombre, apellido):
    persona = Persona(nombre=nombre, apellido=apellido, edad=random.randrange(1,99), fecha_nacimiento=datetime.now())
    persona.save()
    templete = loader.get_template ('crear_persona.html')
    templete_renderizado = templete.render({'persona': persona})
    return HttpResponse (templete_renderizado)

#def crear_persona(request):
#    templete = loader.get_template ('crear_persona.html')
#    templete_renderizado = templete.render(templete_renderizado)
#    return HttpResponse (templete_renderizado)


def ver_personas(request):
    
   personas =  Persona.objects.all()
   templete = loader.get_template ('ver_personas.html')
   templete_renderizado = templete.render({'personas': personas})
   return HttpResponse (templete_renderizado)
