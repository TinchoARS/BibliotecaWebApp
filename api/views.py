from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from biblioteca.models import Empleado, Libro


def listado_libro(request):
    libros = Libro.objects.all()

    libros_data = []
    for libro in libros:
        libro_data = {
            'id': libro.id,
            'titulo': libro.titulo,
            'autor': {
                'nombre': libro.autor.nombre,
                'apellido': libro.autor.apellido,
            },
        }
        libros_data.append(libro_data)
    return JsonResponse(libros_data, safe=False)


def registro_libro(request, id):
    libro = get_object_or_404(Libro, id=id)

    autor_data = {
        'id': libro.autor.id,
        'nombre': libro.autor.nombre,
        'apellido': libro.autor.apellido,
    }

    libro_data = {
        'id': libro.id,
        'titulo': libro.titulo,
        'descripcion': libro.descripcion,
        'autor': autor_data,
    }
    return JsonResponse(libro_data)


def listado_empleado(request):
    empleados = Empleado.objects.all()

    empleados_data = []
    for empleado in empleados:
        empleado_data = {
            'id': empleado.id,
            'nombre': empleado.nombre,
            'apellido': empleado.apellido,
            'numero_legajo': empleado.numero_legajo,
        }
        empleados_data.append(empleado_data)
    return JsonResponse(empleados_data, safe=False)