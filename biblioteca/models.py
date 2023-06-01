from django.db import models
from datetime import date

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=60)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Libro(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=255)
    isbn = models.IntegerField()
    autor = models.ForeignKey(Autor,related_name="libros",on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.titulo}-ISBN:{self.isbn}"

class Socio(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    numero_legajo = models.CharField(max_length=30)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}: {self.numero_legajo}"

class PrestamoLibro(models.Model):
    fecha_prestamo = models.DateField(default=date.today)
    fecha_devolucion = models.DateField(default=date.today)
    socio = models.ForeignKey('Socio', related_name='socio', on_delete=models.CASCADE)
    empleado = models.ForeignKey('Empleado', related_name='empleado', on_delete=models.CASCADE)
    libro = models.ForeignKey('Libro', related_name='libro', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.socio.nombre}"