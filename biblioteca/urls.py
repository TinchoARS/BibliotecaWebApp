from django.urls import path
<<<<<<< HEAD
from .views import saludar,registrar_empleado, desactivar_empleado, desactivar_autor, activar_empleado, listado_empleados, actualizar_datos_empleado
=======
from .views import (registrar_empleado, 
                    desactivar_empleado, 
                    activar_empleado, 
                    listado_empleados, 
                    actualizar_datos_empleado,)
>>>>>>> develop

urlpatterns = [
    path('empleados/registrar',registrar_empleado, name='registrar_empleado'),
    path('empleados/desactivar/<int:id>', desactivar_empleado, name='desactivar_empleado'),
    path('empleados/activar/<int:id>', activar_empleado, name='activar_empleado'),
    path('empleados/listado/', listado_empleados, name='listado_empleados'),
<<<<<<< HEAD
    path('modificar/<int:empleado_id>', actualizar_datos_empleado, name='listado_empleados'),
    path('autores/desactivar/<int: id>', desactivar_autor, name='desactivar_autor')
=======
    path('empleados/actualizar/<int:empleado_id>', actualizar_datos_empleado, name='actualizar_empleado')
>>>>>>> develop
]