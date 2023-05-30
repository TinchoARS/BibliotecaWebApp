from django.urls import path
from .views import registrar_empleado, desactivar_empleado, desactivar_autor, activar_empleado, eliminar_empleado, listado_empleados, listado_autores, actualizar_datos_empleado, nuevo_autores, actualizar_autores, activar_autor, nuevo_socio, listado_socios, eliminar_prestamo_libro , actualizar_datos_socio

urlpatterns = [
    path('empleados/registrar',registrar_empleado, name='registrar_empleado'),
    path('empleados/desactivar/<int:id>', desactivar_empleado, name='desactivar_empleado'),
    path('empleados/activar/<int:id>', activar_empleado, name='activar_empleado'),
    path('empleados/eliminar/<int:id>', eliminar_empleado, name='eliminar_empleado'),
    path('empleados/listado/', listado_empleados, name='listado_empleados'),
    path('empleados/actualizar/<int:empleado_id>', actualizar_datos_empleado, name='actualizar_empleado'),
    path('autores/desactivar/<int:autor_id>', desactivar_autor, name='desactivar_autor'),
    path('autores/nuevo/', nuevo_autores, name='nuevo_autores'),
    path('autores/actualizar/<int:autor_id>/', actualizar_autores, name='actualizar_autores'),
    path('autores/activar/<int:autor_id>/', activar_autor, name='activar_autor'),
    path('autores/listado/', listado_autores, name='listado_autores'),
    path('socios/nuevo/', nuevo_socio, name='nuevo_socio'),
    path('socios/listado/', listado_socios, name='listado_socios'),
    path('socios/actualizar/<int:socio_id>',actualizar_datos_socio,name='actualizar_datos_socio'),
    path('prestamos/eliminar/<int:prestamo_id>', eliminar_prestamo_libro, name='eliminar_prestamo_libro'),
]