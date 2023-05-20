from django.shortcuts import render,HttpResponse
from biblioteca.models import Empleado

# Create your views here.
def saludar(request):
    return HttpResponse("hola")

def registrar_empleado(request):
    listadoDeEmpleados=Empleado.objects.all()
    context = {
        "listadoDeEmpleados":listadoDeEmpleados
    }
    if request.POST:
        nombre_empleado = request.POST["nombre"]
        apellido_empleado = request.POST["apellido"]
        numeroLeg_empleado = request.POST["numero_legajo"]

        Empleado.objects.create(
        nombre=nombre_empleado,
        apellido=apellido_empleado,
        numero_legajo=numeroLeg_empleado
        )
    return render(request,"biblioteca/registrar_empleado.html",context)
