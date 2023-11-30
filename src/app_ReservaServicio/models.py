from django.db import models
from django.urls import reverse
# Create your models here.
class ReservaServicio(models.Model):
    fecha_reserva = models.DateField((""), auto_now=False, auto_now_add=False)
    fecha_servicio = models.DateField((""), auto_now=False, auto_now_add=False)
    cliente = models.CharField(max_length=30)
    sevicio = models.TextField()  
    empleado = models.CharField(max_length=30)
    cordinador = models.CharField(max_length=30)
        
    def __str__(self):
        return F"{self.fecha_reserva} - {self.fecha_servicio} - {self.cliente} - {self.servicio} - {self.empleado} - {self.cordinador}"
 