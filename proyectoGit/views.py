

from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template, loader
import random


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



