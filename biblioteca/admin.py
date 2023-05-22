from django.contrib import admin
from biblioteca.models import Socio,Autor,Libro,Prestamo_Libro,Empleado

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

class LibroAdmin(admin.ModelAdmin):
    model= Libro
    
    list_display=[
    "isbn",
    "titulo",
    "autor",
    "activo",
    ]
    
    search_fields = [
        "titulo",
        
    ]
    list_filter = [
        "activo"
    ]
class Prestamo_LibroAdmin(admin.ModelAdmin):
    model = Prestamo_Libro

    list_display=[
        "fecha_prestamo",
        "fecha_devolucion",
        "socio",
        "empleado",
        "libro",
    ]
    search_fields = [
        'Socio__nombre',
        'Libro__titulo',
        'Empleado__nombre'
    ]

class EmpleadoAdmin(admin.ModelAdmin):
    model = Empleado
    
    list_display=[
        "nombre",
        "apellido",
        "numero_legajo",
        "activo",
    ]
    list_search = [
        "nombre",
        "apellido",
    ]
    list_filter = [
        "activo"
    ]
    
    
    
    

admin.site.register(Socio,SocioAdmin)
admin.site.register(Autor,Autor_admin)
admin.site.register(Libro,LibroAdmin)
admin.site.register(Prestamo_Libro,Prestamo_LibroAdmin)
admin.site.register(Empleado,EmpleadoAdmin)