from django.urls import path
from .views import registrar_empleado, desactivar_empleado, desactivar_autor, activar_empleado, listado_empleados, listado_autores, actualizar_datos_empleado, nuevo_autores, actualizar_autor, activar_autor,desactivar_socio

urlpatterns = [
    path('empleados/registrar',registrar_empleado, name='registrar_empleado'),
    path('empleados/desactivar/<int:id>', desactivar_empleado, name='desactivar_empleado'),
    path('empleados/activar/<int:id>', activar_empleado, name='activar_empleado'),
    path('empleados/listado/', listado_empleados, name='listado_empleados'),
    path('empleados/actualizar/<int:empleado_id>', actualizar_datos_empleado, name='actualizar_empleado'),
    path('autores/desactivar/<int:id>', desactivar_autor, name='desactivar_autor'),
    path('autores/nuevo/', nuevo_autores, name='nuevo_autores'),
    path('autores/actualizar/<int:id>/', actualizar_autor, name='actualizar_autor'),
    path('autores/activar/<int:id>/', activar_autor, name='activar_autor'),
    path('autores/listado/', listado_autores, name='listado_autores'),
    path('socio/desactivar/<int:id>/', desactivar_socio, name='desactivar_socio'),
]