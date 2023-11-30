from django.db import models
from django.urls import reverse

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return F"{self.nombre} | {self.apellido} {self.activo}"
    
def get_absolute_url(self):
    return reverse('clientes:detalle', kwargs={'pk': self.id})