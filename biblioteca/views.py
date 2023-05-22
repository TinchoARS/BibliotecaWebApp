
from django.shortcuts import render,get_object_or_404, HttpResponse

from django.shortcuts import render,HttpResponse

from biblioteca.models import Empleado

# Create your views here.
def saludar(request):
    return HttpResponse("hola")


def desactivar_empleado(request, id):
    Empleado= get_object_or_404(Empleado, id=id)
    
    if Empleado.activo:
        Empleado.activo=False
        Empleado.save()
        mensaje= "Empleado desactivado correctamente"
    else:
        mensaje= "Empleado ya esta desactivado"
    
    return render(request, 'desactivar_empleado.html',{'mensaje':mensaje})

def activar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)

    if not empleado.activo:
        empleado.activo = True
        empleado.save()
        mensaje = "Empleado activado correctamente."
    else:
        mensaje = "Empleado ya está activo."

    return render(request, 'mensaje_activacion.html', {'mensaje': mensaje})

def registrar_empleado(request):
    if request.POST:
        nombre_empleado = request.POST["nombre"]
        apellido_empleado = request.POST["apellido"]
        numeroLeg_empleado = request.POST["numero_legajo"]

        Empleado.objects.create(
        nombre=nombre_empleado,
        apellido=apellido_empleado,
        numero_legajo=numeroLeg_empleado
        )
    return render(request,"biblioteca/nuevos_empleados.html")

def listado_empleados(request):
    lista_empleados = Empleado.objects.all()

    context= {
        "lista_empleados" : lista_empleados
    }
    return render(
        request,
        "biblioteca/listado_empleados.html",
        context,
    )