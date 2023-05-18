from django.db import models

class Libro(models.Model):
    titulo=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=255)
    isbn=models.IntegerField()
    autor=models.ForeignKey(Autor,related_name="autor",on_delete=models.CASCADE)
    activo=models.BooleanField(default=True)

# Create your models here.
class Socio(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    fecha_nacimiento=models.DateField
    activo=models.BooleanField(default=True)

