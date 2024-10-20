from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class Vehiculo(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20)
    precio = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.marca} {self.modelo} {self.serial_carroceria} {self.serial_motor} {self.categoria} {self.precio} {self.fecha_creacion} {self.fecha_modificacion}"

    class Meta:
        permissions = [
            ("visualizar_catalogo", "Can view catalog of vehicles"),
        ]