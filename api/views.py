from django.shortcuts import render
from django.http import JsonResponse

from biblioteca.models import Libro

def listado_libro(request):
    libros = Libro.objects.all()

    libros_data = []
    for libro in libros:
        libro_data = {
            'id': libro.id,
            'titulo': libro.titulo,
            'autor': libro.autor,
        }
        libros_data.append(libro_data)

   
    return JsonResponse(libros_data)
