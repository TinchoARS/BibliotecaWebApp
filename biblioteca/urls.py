from django.urls import path
from .views import saludar,registrar_empleado

urlpatterns = [
    path('example/', saludar, name='saludar'),
    path('empleados/nuevo',registrar_empleado, name='registrar_empleado')
]