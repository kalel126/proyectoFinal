
from django.urls import path
from home import views 

urlpatterns = [
    
    path('',  views.index, name='index'),
    path('productos/',  views.productos, name='productos'),
    path('aboutus/',  views.aboutus, name='aboutus'),
    path('login/',  views.login, name='login'),
    path('admin_productos/',  views.admin_productos, name='admin_productos'),
    path('crear_productos/',  views.crear_productos, name='crear_productos'),
    
    
    
    path('hola/',  views.hola),
    path('fecha/',  views.fecha, name='fecha'),
    path('mi-template/',  views.mi_template),
    path('ver_personas/',  views.ver_personas,name='ver_personas'),
    path('crear_persona/<str:nombre>/<str:apellido>/',  views.crear_persona),
    path('ver_productos/',  views.ver_productos,name='ver_productos'),
    
]


    