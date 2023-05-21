from django.urls import path
from .views import saludar,registrar_empleado, desactivar_empleado, activar_empleado

urlpatterns = [
    path('example/', saludar, name='saludar'),
    path('empleados/nuevo',registrar_empleado, name='registrar_empleado'),
    path('empleados/desactivar/<int:id>', desactivar_empleado, name='desactivar_empleado'),
    path('empleados/activar/<int:id>', activar_empleado, name='activar_empleado')
]