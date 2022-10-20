
from django.urls import path
from home import views 

urlpatterns = [
    
    path('',  views.index, name='index'),
    path('hola/',  views.hola),
    path('fecha/',  views.fecha, name='fecha'),
    path('mi-template/',  views.mi_template),
    path('ver_personas/',  views.ver_personas,name='ver_personas'),
    path('crear_persona/<str:nombre>/<str:apellido>/',  views.crear_persona),
    
]


    