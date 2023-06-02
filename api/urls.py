from django.urls import path

from .views import listado_libro

urlpatterns = [
    path('api/libros/', listado_libro, name='listado_libros'),
]