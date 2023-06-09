from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from biblioteca.models import Autor, Empleado, Libro, Socio


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


def listado_socio(request):
    socios = Socio.objects.all()
    
    socios_data = []
    for socio in socios:
        socio_data = {
            'id': socio.id,
            'nombre': socio.nombre,
            'apellido': socio.apellido,
            'fecha_nacimiento': socio.fecha_nacimiento,
        }
        socios_data.append(socio_data)
    return JsonResponse(socios_data, safe=False)


def listado_autor(request):
    autores = Autor.objects.all()
    
    autores_data = []
    for autor in autores:
        autor_data = {
            'id': autor.id,
            'nombre': autor.nombre,
            'apellido': autor.apellido,
            'nacionalidad': autor.nacionalidad,
        }
        autores_data.append(autor_data)
    return JsonResponse(autores_data, safe=False)

