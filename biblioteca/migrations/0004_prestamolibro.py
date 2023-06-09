# Generated by Django 4.2.1 on 2023-05-19 14:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_empleado_socio_fecha_nacimiento_alter_libro_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrestamoLibro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamos', models.DateField(default=datetime.date.today)),
                ('fecha_devolucion', models.DateField(default=datetime.date.today)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Empleado', to='biblioteca.empleado')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libro', to='biblioteca.libro')),
                ('socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Socio', to='biblioteca.socio')),
            ],
        ),
    ]
