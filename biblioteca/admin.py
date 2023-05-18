from django.contrib import admin
from biblioteca.models import Socio,Autor

class SocioAdmin(admin.ModelAdmin):
    model= Socio
    
    list_display=[
    "nombre",
    "apellido",
    "fecha_nacimiento",
    "activo",
    ]
    
    search_fields = [
        "nombre",
        "apellido",
        
    ]
    list_filter = [
        "activo"
    ]
class Autor_admin(admin.ModelAdmin):
    model = Autor
    
    list_display=[
    'nombre',
    'apellido',
    'nacionalidad',
    'activo',
    ]

    search_fields = [
        'nombre',
        'apellido',
        
    ]

    list_filter = [
        'activo',
        'nacionalidad',
    ]

admin.site.register(Socio,SocioAdmin)
admin.site.register(Autor,Autor_admin)