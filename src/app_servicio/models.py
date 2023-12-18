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

    def get_absolute_url(self):
        return reverse('servicios:detalle', kwargs={'pk': self.id})

    def get_absolute_url_desactivar(self):
        return reverse('servicios:desactivar', kwargs={"pk": self.id})

    def get_absolute_url_mod(self):
        return reverse('servicios:modificar', kwargs={"pk": self.pk})
