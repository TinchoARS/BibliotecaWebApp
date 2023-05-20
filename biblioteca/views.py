from django.shortcuts import render,get_object_or_404, HttpResponse
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