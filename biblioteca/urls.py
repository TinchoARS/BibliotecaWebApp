from django.urls import path
from .views import (registrar_empleado, 
                    desactivar_empleado, 
                    activar_empleado, 
                    listado_empleados, 
                    actualizar_datos_empleado,)

urlpatterns = [
    path('empleados/registrar',registrar_empleado, name='registrar_empleado'),
    path('empleados/desactivar/<int:id>', desactivar_empleado, name='desactivar_empleado'),
    path('empleados/activar/<int:id>', activar_empleado, name='activar_empleado'),
    path('empleados/listado/', listado_empleados, name='listado_empleados'),
    path('empleados/actualizar/<int:empleado_id>', actualizar_datos_empleado, name='listado_empleados')
]