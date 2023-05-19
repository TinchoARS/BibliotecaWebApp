from django.db import models
from datetime import date

class Autor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    nacionalidad=models.CharField(max_length=60)
    activo=models.BooleanField(default=True)

class Libro(models.Model):
    titulo=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=255)
    isbn=models.IntegerField()
    autor=models.ForeignKey(Autor,related_name="libros",on_delete=models.CASCADE)
    activo=models.BooleanField(default=True)

class Socio(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    fecha_nacimiento=models.DateField(default=date.today)
    activo=models.BooleanField(default=True)

class Empleado(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    numero_legajo=models.CharField(max_length=30)
    activo=models.BooleanField(default=True)
    
class PrestamoLibro(models.Model):
    fecha_prestamos=models.DateField(default=date.today)
    fecha_devolucion=models.DateField(default=date.today)
    socio=models.ForeignKey(Socio,related_name='Socio',on_delete=models.CASCADE)
    empleado=models.ForeignKey(Empleado,related_name='Empleado', on_delete=models.CASCADE)
    libro=models.ForeignKey(Libro,related_name='libro', on_delete=models.CASCADE)
