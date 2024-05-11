from django.contrib.auth.models import User
from django.db import models


class Responsable(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.cargo}"


class Dispositivo(models.Model):
    serial = models.CharField(max_length=50)
    tipo_dispositivo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    activo_viejo = models.CharField(max_length=25, unique=True)
    activo_nuevo = models.CharField(max_length=50, unique=True)
    ubicacion = models.CharField(max_length=100)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.serial} - {self.tipo_dispositivo} - {self.marca} - {self.modelo} - {self.ubicacion}"


class Servicio(models.Model):
    CHOICES = (
        ('error', 'Error'),
        ('mejora', 'Mejora'),
        ('nueva funcion', 'Nueva Funcion'),
    )
    tipo_servicio = models.CharField(max_length=100, choices=CHOICES)
    requerimiento = models.CharField(max_length=200)
    solucion = models.TextField(max_length=1000)
    fecha = models.DateTimeField("fecha_servicio", auto_now_add=True)
    dispositivos = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo_servicio} - {self.requerimiento} - {self.solucion} - {self.fecha}"


class Tecnico(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)