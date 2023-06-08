from django.urls import path

from .views import listado_empleado, listado_libro, registro_libro

urlpatterns = [
    path('empleados/', listado_empleado, name='listado_empleado'),
    path('libros/', listado_libro, name='listado_libro'),
    path('libros/<int:id>', registro_libro, name='registro_libro'),
]