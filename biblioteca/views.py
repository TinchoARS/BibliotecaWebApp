from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from biblioteca.models import Empleado, Autor, Socio, PrestamoLibro , Libro
from datetime import datetime, timedelta
# Create your views here.
        
def desactivar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    
    if empleado.activo:
        empleado.activo = False
        empleado.save()
        
    
    return redirect("listado_empleados")

def activar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)

    if not empleado.activo:
        empleado.activo = True
        empleado.save()

    return redirect("listado_empleados")

def eliminar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    empleado.delete()
    return redirect("listado_empleados")

def registrar_empleado(request):
    if request.POST:
        nombre_empleado = request.POST["nombre"]
        apellido_empleado = request.POST["apellido"]
        numeroLeg_empleado = request.POST["numero_legajo"]

        Empleado.objects.create(
        nombre = nombre_empleado,
        apellido = apellido_empleado,
        numero_legajo = numeroLeg_empleado
        )
    return render(request,"biblioteca/nuevos_empleados.html")

def listado_empleados(request):
    lista_empleados = Empleado.objects.all()

    return render(request, "biblioteca/listado_empleados.html", {"lista_empleados" : lista_empleados})

def actualizar_datos_empleado(request, empleado_id):
    empleado = Empleado.objects.get(id=empleado_id)

    if request.POST:
        nombre_empleado = request.POST["nombre"]
        apellido_empleado = request.POST["apellido"]
        numeroLeg_empleado = request.POST["numero_legajo"]

        empleado.nombre = nombre_empleado
        empleado.apellido = apellido_empleado
        empleado.numero_legajo = numeroLeg_empleado

        empleado.save()

    return render(request, "biblioteca/actualizar_empleado.html", {"empleado" : empleado})

def desactivar_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    autor.activo=False
    autor.save()
    return redirect("listado_autores")   

def nuevo_autores(request):
    if request.POST:
        nombre_autor = request.POST["nombre"]
        apellido_autor = request.POST["apellido"]
        nacionalidad_autor = request.POST["nacionalidad"]

        Autor.objects.create(
        nombre = nombre_autor,
        apellido = apellido_autor,
        nacionalidad = nacionalidad_autor
        )
        return redirect("listado_autores")
    return render(request,"biblioteca/nuevos_autores.html")

def actualizar_autores(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)

    if request.method == 'POST':

        nombre_autor = request.POST.get('nombre')
        apellido_autor = request.POST.get('apellido')
        nacionalidad_autor = request.POST.get('nacionalidad')

        autor.nombre = nombre_autor
        autor.apellido = apellido_autor
        autor.nacionalidad = nacionalidad_autor
        autor.save()
        return redirect("listado_autores")

    context = {'autor': autor}
    return render(request, 'biblioteca/actualizar_autor.html', context)

def activar_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    autor.activo = True
    autor.save()
    return redirect("listado_autores")

def listado_autores(request):
    lista_autores = Autor.objects.all()

    return render(request, "biblioteca/listado_autores.html", {"lista_autores" : lista_autores})

def nuevo_socio(request):
    if request.POST:
        nombre_socio = request.POST["nombre"]
        apellido_socio = request.POST["apellido"]
        fecha_nacimiento_socio = request.POST["fecha_nacimiento"]
        
        Socio.objects.create(
        nombre = nombre_socio,
        apellido = apellido_socio,
        fecha_nacimiento = fecha_nacimiento_socio
        )
    return render(request, "biblioteca/nuevo_socios.html")

def listado_socios(request):
    lista_socios = Socio.objects.all()

    return render(request, "biblioteca/listado_socios.html", {"lista_socios" : lista_socios})

def eliminar_prestamo_libro(request, prestamo_id):
    prestamo_libro = get_object_or_404(PrestamoLibro, id=prestamo_id)
    prestamo_libro.delete()
    return redirect("listado_prestamos")



def actualizar_datos_socio(request, socio_id):

    socio = get_object_or_404(Socio, id=socio_id)

    if request.method == 'POST':
        nombre_socio = request.POST['nombre']
        apellido_socio = request.POST['apellido']
        fecha_nacimiento_socio = request.POST['fecha_nacimiento']
        socio.nombre = nombre_socio
        socio.apellido = apellido_socio
        fecha_dt = datetime.strptime(fecha_nacimiento_socio,'%Y-%m-%d')
        socio.fecha_nacimiento= fecha_dt
        socio.save()
        
    context = {'socio': socio}
    return render(request, 'biblioteca/actualizar_socio.html', context)

def activar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    libro.activo = True
    libro.save()
    return redirect("listado_libros")

def activar_socio(request, id):
    socio = get_object_or_404(Socio, id=id)
    socio.activo = True
    socio.save()

    return HttpResponse("El socio está activo")

def desactivar_socio(request, id):
    socio = get_object_or_404(Socio, id=id)
    socio.activo=False
    socio.save()
    return redirect("listado_socios")   

def nuevo_libro(request):
    listado_autores= Autor.objects.all()
    if request.POST:
        titulo_libro = request.POST["titulo"]
        descripcion_libro = request.POST["descripcion"]
        isbn_libro = request.POST["isbn"]
        autor_libro=request.POST["autor"]
                
        Libro.objects.create(
        titulo = titulo_libro,
        descripcion = descripcion_libro,
        isbn = isbn_libro,
        autor= Autor.objects.get(id=autor_libro)
        )
    context = {'listado_autores':listado_autores}
    return render(request, "biblioteca/nuevos_libros.html", context)

def listado_libros(request):
    listado_libros = Libro.objects.all()
    context = {"listado_libros" : listado_libros}

    return render(request, "biblioteca/listado_libros.html", context )

def desactivar_libro(request,id):
    libro = get_object_or_404(Libro, id=id)
    libro.activo=False
    libro.save()
    return redirect("listado_libros")   

def actualizar_libro(request, id):

    libro = get_object_or_404(Libro, id=id)
    listado_autores= Autor.objects.all()

    if request.method == 'POST':
        titulo_libro = request.POST['titulo']
        descripcion_libro = request.POST['descripcion']
        isbn_libro = request.POST['isbn']
        autor_libro= Autor.objects.get(id=request.POST['autor'])
        libro.titulo = titulo_libro
        libro.descripcion = descripcion_libro
        libro.isbn = isbn_libro
        libro.autor = autor_libro

        libro.save()
        
    context = {'libro': libro,'listado_autores' : listado_autores }
    return render(request, 'biblioteca/actualizar_libro.html', context)
def listado_prestamos(request):
    listado_prestamos = PrestamoLibro.objects.all()
    context = {"listado_prestamos" : listado_prestamos}

    return render(request, "biblioteca/listado_prestamos.html", context )

def registrar_prestamo(request):
    if request.POST:
        fecha_Prestamo = datetime.strptime(request.POST["fecha_prestamo"],"%Y-%m-%d").date()
        socio=request.POST["socio"]
        empleado=request.POST["empleado"]
        libro=request.POST["libro"]

        fecha_devolucion= fecha_Prestamo + timedelta(days=2)
        fecha_devolucion_str = fecha_devolucion.strftime("%Y-%m-%d")  # Convertir a cadena

        PrestamoLibro.objects.create(
        fecha_prestamo = fecha_Prestamo,
        fecha_devolucion =fecha_devolucion_str,
        socio_id=socio,
        empleado_id=empleado,
        libro_id=libro,
        )

    return render(request, "biblioteca/nuevos_prestamo_libro.html", {
    'lista_empleados': Empleado.objects.all(),
    'lista_socios': Socio.objects.all(),
    'lista_libros': Libro.objects.all()
    })

def actualizar_prestamo(request, id):
    prestamo = get_object_or_404(PrestamoLibro, id=id)
    listado_empleados= Empleado.objects.all()
    listado_libros= Libro.objects.all()
    listado_socios= Socio.objects.all()
    if request.method == 'POST':
        empleado_prestamo = Empleado.objects.get(id=request.POST['empleado'])
        socio_prestamo = Socio.objects.get(id=request.POST['socio'])
        libro_prestamo = Libro.objects.get(id=request.POST['libro'])
        prestamo.empleado = empleado_prestamo
        prestamo.socio = socio_prestamo
        prestamo.libro = libro_prestamo
        prestamo.save()

    context = {'prestamo': prestamo,
            'listado_empleados' : listado_empleados,
            'listado_libros' : listado_libros,
            'listado_socios' : listado_socios 
    }
    return render(request, 'biblioteca/actualizar_prestamo.html', context)
    
def actualizar_prestamo(request, id):
    prestamo = get_object_or_404(PrestamoLibro, id=id)
    listado_empleados= Empleado.objects.all()
    listado_libros= Libro.objects.all()
    listado_socios= Socio.objects.all()
    if request.method == 'POST':
        empleado_prestamo = Empleado.objects.get(id=request.POST['empleado'])
        socio_prestamo = Socio.objects.get(id=request.POST['socio'])
        libro_prestamo = Libro.objects.get(id=request.POST['libro'])
        prestamo.empleado = empleado_prestamo
        prestamo.socio = socio_prestamo
        prestamo.libro = libro_prestamo
        prestamo.save()

    context = {'prestamo': prestamo,
            'listado_empleados' : listado_empleados,
            'listado_libros' : listado_libros,
            'listado_socios' : listado_socios 
    }
    return render(request, 'biblioteca/actualizar_prestamo.html', context)