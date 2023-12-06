from django.db import models
from django.urls import reverse
# Create your models here.


class Servicio(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=300)
    precio = models.FloatField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return F"{self.nombre} "
