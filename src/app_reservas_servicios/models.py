from django.db import models
from django.urls import reverse
from app_servicio.models import Servicio
from app_empleados.models import Empleado
from app_coordinadores.models import Coordinador
from app_clientes.models import Cliente
# Create your models here.


class ReservaServicio(models.Model):
    fecha_reserva = models.DateField((""), auto_now=False, auto_now_add=False)
    fecha_servicio = models.DateField((""), auto_now=False, auto_now_add=False)
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, default=None)
    servicio = models.ForeignKey(
        Servicio, on_delete=models.CASCADE, default=None)
    empleado = models.ForeignKey(
        Empleado, on_delete=models.CASCADE, default=None)
    coordinador = models.ForeignKey(
        Coordinador, on_delete=models.CASCADE, default=None)

    def __str__(self) -> str:
        return F"Cliente: {self.cliente} - Servicio: {self.servicio} - Coordinador: {self.coordinador} - Empleado: {self.empleado} "
    
    def get_absolute_url_eliminar(self):
        return reverse('reserva_servicios:eliminar', kwargs={"pk": self.id})

    def get_absolute_url_mod(self):
        return reverse('reserva_servicios:modificar', kwargs={"pk": self.pk})
