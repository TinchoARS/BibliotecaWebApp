from django.db import models

# Create your models here.
class Socio(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    fecha_nacimiento=models.DateField
    activo=models.BooleanField(default=True)
