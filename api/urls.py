from django.urls import path

from .views import listado_autor, listado_empleado, listado_libro, listado_socio, registro_libro

urlpatterns = [
    path('autores/', listado_autor, name='listado_autor'),
    path('empleados/', listado_empleado, name='listado_empleado'),
    path('libros/', listado_libro, name='listado_libro'),
    path('socios/', listado_socio, name='listado_socio'),
    path('libros/<int:id>', registro_libro, name='registro_libro'),
    
]