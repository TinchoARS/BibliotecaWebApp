from django.contrib import admin
from biblioteca.models import Socio

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

admin.site.register(Socio,SocioAdmin)