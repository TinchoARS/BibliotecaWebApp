from django.shortcuts import render, get_object_or_404, redirect
from biblioteca.models import Empleado, Autor, Socio

# Create your views here.
def nuevo_empleado(request):
    if request.POST:
        nombre_empleado = request.POST["nombre"]
        apellido_empleado = request.POST["apellido"]
        numero_legajo = request.POST["numero_legajo"]
        
        Empleado.objects.create(
        nombre=nombre_empleado,
        apellido=apellido_empleado,
        numero_legajo=numero_legajo
        )
        return redirect("listado_empleados")
    return render(request, "biblioteca/nuevo_empleado.html")
        
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
    return render(request, "biblioteca/nuevos_socios.html")

def listado_socios(request):
    lista_socios = Socio.objects.all()

    return render(request, "biblioteca/listado_socios.html", {"lista_socios" : lista_socios})