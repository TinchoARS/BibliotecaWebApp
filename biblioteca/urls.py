from django.urls import path
from .views import saludar,desactivar_empleado

urlpatterns = [
    path('example/', saludar, name='saludar'),
    # Add more URL patterns here
    path('empleados/desactivar/<int:id>', desactivar_empleado, name='desactivar_empleado'),
]