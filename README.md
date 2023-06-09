# Aceleración DJANGO/Python  - Biblioteca 
> ## Introducción:
El siguiente proyecto está desarrollado en el marco de la aceleración llevada adelante por el **Gobierno de Salta** a través de la empresa **ALKEMY** para los egresados de 1000 Programadores y Programadoras

El [Caso de Negocio](https://drive.google.com/file/d/19xcxerwFI-RS_HVLMU0wVqOp0k_XqGDu/) que se desarrollo es el de una **Bilbioteca** que presta libros, tiene socios y empleados. Su objetivo es gestionar los prestamos de libros.

>## Alcance:
Desde la configuración inicial de las entidades libro, autor, empleado y socio , su gestión; hasta la registración de un prestamo de libro.

> ## Tenoclogía y Lenguajes utilizados:
- FrameWork DJANGO
- Python
- Jinga2
- HTML/Boostrap
- SQLLite3
- Git
- Jira




> ## Funcionalidades:

>>### ***Módulo Empleados:***
Este módulo permite resgistrar, modificar, elimanar lógicamente y mostrar a todos los empleados de la Biblioteca. Básicamente es un **CRUD de empleados**.

Modelo de Datos:

```python
class Empleado(models.Model):
        nombre = models.CharField(max_length=30)
        apellido = models.CharField(max_length=30)
        numero_legajo = models.CharField(max_length=30)
        activo = models.BooleanField(default=True)
        # el campo 'activo' sirve para el borrrado lógico de la entidad
        def __str__(self):
            return f"{self.nombre} {self.apellido}: {self.numero_legajo}"
```

### **Registar Empleado:**

<picture>
  <img alt="Pantalla para registrar un empleado" src="Imagenes/registrarempleado.png">
</picture>

Esta pantalla permite registrar un nuevo empleado ingresando Nombre, Apellido y Número de Legajo. 

[Acceso:](http://localhost:8000/biblioteca/empleados/nuevo) puede acceder al formulario desde la url http://localhost:8000/biblioteca/empleados/nuevo , desde el formulario "Listado de Empleados" o desde la ["Home Page"](http://localhost:8000/biblioteca/pagina_principal/)

Vista:
```python
    def registrar_empleado(request):
        if request.POST:
          # Se cargan las variables con los datos que se reciben desde el formulario por el método POST
            nombre_empleado = request.POST["nombre"]
            apellido_empleado = request.POST["apellido"]
            numeroLeg_empleado = request.POST["numero_legajo"]

            # Se crea el objeto de la clase 'Empleado' con los datos de las variables y este se registra en la base de datos.
            Empleado.objects.create(
            nombre=nombre_empleado,
            apellido=apellido_empleado,
            numero_legajo=numeroLeg_empleado
            )
            # Se renderiza y retornamos el request al templeate 'nuevo empleado'
        return render(request,"biblioteca/nuevos_empleados.html")
```


### **Listar Empleados:**

<picture>
  <img alt="Pantalla para listar empleados" src="Imagenes/listarempleados.png">
</picture>
Esta pantalla permite listar a todos los empleado, tanto activos como inactivos de la biblioteca y poder gestionar la actualización de sus datos, activar o desartivar su estado y/o agregar un nuevo empleado.

[Acceso:](http://localhost:8000/biblioteca/empleados/listado) puede acceder al formulario desde la url http://localhost:8000/biblioteca/empleados/listado , desde el formulario "Listado de Empleados" o desde la ["
Home Page"](http://localhost:8000/biblioteca/pagina_principal/)

Vista:
```python
def listado_empleados(request):
   # Se cargan todos los registros de empleados de la base a la variable lista_empleados
    lista_empleados = Empleado.objects.all()

    #Se renderiza y se envían la lista con todos los empleados al template 'listado de empleados'
    return render(request, "biblioteca/listado_empleados.html", {"lista_empleados" : lista_empleados})
```
### **Actualizar Empleado:**
<picture>
  <img alt="Pantalla para la actulizar empleados" src="Imagenes/actualizarempleado.png">
</picture>
Esta pantalla permite actualizar el nombre, apellido y nro. de legajo de un empleado seleccionado desde la pantalla 'listado de empleados' 

Acceso: puede acceder al formulario desde la url http://localhost:8000/biblioteca/empleados/listado , haciendo clic sobre el botón 'Actualizar'

Vista:
```python
def actualizar_empleado(request, empleado_id):
    # Se cargan los datos de la base correspondientes con el id del empleado seleccionado desde el template 'listado de empleados' en la variable empleado

    empleado = Empleado.objects.get(id=empleado_id)

    if request.POST:
      # Se cargan las variables con los datos que se reciben desde el formulario por el método POST

        nombre_empleado = request.POST["nombre"]
        apellido_empleado = request.POST["apellido"]
        numeroLeg_empleado = request.POST["numero_legajo"]

        # Se actualiza el objeto 'empleado' con los datos recibidos del formulario

        empleado.nombre=nombre_empleado
        empleado.apellido=apellido_empleado
        empleado.numero_legajo=numeroLeg_empleado
        empleado.save()

        # Se retorna a la página con el listado de empleados actualizada
        return redirect("listado_empleados")
    # Se renderiza y retornamos el request al templeate 'actualizar empleado' con los datos del objeto 'empleado'
    return render(request, "biblioteca/actualizar_empleado.html", {"empleado" : empleado})
```
>>### ***Módulo Prestamos de libros:***
Este módulo permite resgistrar, modificar, eliminar  y mostrar a todos los prestamos de libros de la Biblioteca.

Modelo de Datos:
```python 
class PrestamoLibro(models.Model):
    fecha_prestamo = models.DateField(default=date.today)
    fecha_devolucion = models.DateField(default=date.today)
    socio = models.ForeignKey('Socio', related_name='socio', on_delete=models.CASCADE)
    empleado = models.ForeignKey('Empleado', related_name='empleado', on_delete=models.CASCADE)
    libro = models.ForeignKey('Libro', related_name='libro', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.socio.nombre}"
        #Devuelve una cadena que representa el nombre del socio asociado al préstamo. Esto se utiliza para mostrar el nombre del socio cuando se imprime o se muestra una instancia de PrestamoLibro.
```
### **Registar Prestamo:**
<picture>
  <img alt="Pantalla para registrar un prestamo" src="Imagenes/registrarprestamo.png">
</picture>
Esta pantalla permite registrar un nuevo prestamo ingresando fecha de prestamo, nombre del empleado , socio y el libro.

[Acceso:](http://localhost:8000/biblioteca/prestamos/nuevo) puede acceder al formulario desde la url http://localhost:8000/biblioteca/prestamos/nuevo, desde el formulario "Listado de Prestamos" o desde la ["
Home Page"](http://localhost:8000/biblioteca/pagina_principal/)

Vista:
```python
def registrar_prestamo(request):
    if request.POST:
        fecha_Prestamo = datetime.strptime(request.POST["fecha_prestamo"],"%Y-%m-%d").date()
        socio=request.POST["socio"]
        empleado=request.POST["empleado"]
        libro=request.POST["libro"]

        fecha_devolucion = fecha_Prestamo + timedelta(days=2)
        fecha_devolucion_str = fecha_devolucion.strftime("%Y-%m-%d")  # Convertir a cadena

        PrestamoLibro.objects.create(
        fecha_prestamo=fecha_Prestamo,
        fecha_devolucion=fecha_devolucion_str,
        socio_id=socio,
        empleado_id=empleado,
        libro_id=libro,
        )

    return render(request, "biblioteca/nuevos_prestamo_libro.html", {
    'lista_empleados': Empleado.objects.all(),
    'lista_socios': Socio.objects.all(),
    'lista_libros': Libro.objects.all()
    })

```
### **Listar Prestamos:**
<picture>
  <img alt="Pantalla para registrar un prestamo" src="Imagenes/listadoprestamos.png">
</picture>
Esta pantalla permite listar a todos los prestamos, poder gestionar la actualización ,eliminar  y/o agregar un nuevo prestamo.

[Acceso:](http://localhost:8000/biblioteca/prestamos/listado) puede acceder al formulario desde la url http://localhost:8000/biblioteca/prestamos/listado , desde el formulario "Listado de Empleados" o desde la ["
Home Page"](http://localhost:8000/biblioteca/pagina_principal/)

Vista:
```python
def listado_prestamos(request):
  # Se cargan todos los registros de prestamos de la base a la variable listado_prestamos
    listado_prestamos = PrestamoLibro.objects.all()
  #Aquí se crea un diccionario llamado context que contiene una clave llamada "listado_prestamos" cuyo valor es la lista de préstamos obtenida en el paso anterior. Este diccionario se utiliza para pasar información adicional
    context = {"listado_prestamos" : listado_prestamos}
    #Se renderiza y se envían la lista con todos los prestamos al template 'listado de prestamos'
    return render(request, "biblioteca/listado_prestamos.html", context )
```
### **Actualizar Prestamo:**
<picture>
  <img alt="Pantalla para actualizar un prestamo" src="Imagenes/actualizarprestamo.png">
</picture>
Esta pantalla permite actualizar el libro, socio y el empleado. seleccionado desde la pantalla 'listado de prestamos' 

Acceso: puede acceder al formulario desde la url http://localhost:8000/biblioteca/prestamos/listado , haciendo clic sobre el botón 'Actualizar'

Vista:
```python
def actualizar_prestamo(request, id):
    prestamo = get_object_or_404(PrestamoLibro, id=id)
    listado_empleados= Empleado.objects.all()
    listado_libros= Libro.objects.all()
    listado_socios= Socio.objects.all()
    
    if request.method == 'POST':
        empleado_prestamo = Empleado.objects.get(id=request.POST['empleado'])
        socio_prestamo = Socio.objects.get(id=request.POST['socio'])
        libro_prestamo = Libro.objects.get(id=request.POST['libro'])
        
        prestamo.empleado=empleado_prestamo
        prestamo.socio=socio_prestamo
        prestamo.libro=libro_prestamo
        prestamo.save()
        return redirect("listado_prestamos")
    
    context = {'prestamo': prestamo,
            'listado_empleados' : listado_empleados,
            'listado_libros' : listado_libros,
            'listado_socios' : listado_socios 
    }
    
    return render(request, 'biblioteca/actualizar_prestamo.html', context)

```
>## Autores:
**Comision 4 Squad 2**
- Arredes Javier Ricardo
- Cayampi Segovia Ismael Braian
- Fradejas Soria Martín
- Villa Cristian Nahuel
- Ulloa Pablo Alfredo
