from django.db import models
from django.urls import reverse

# Create your models here.


class Cliente(models.Model):

    
    """Representa el modelo de un cliente.

    Atributos:
        nombre (str): [nombre]
        apellido (str): [apellido]
        activo(bool): [activo]

    """

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return F"{self.nombre} {self.apellido}"
    
    """Inicializa el objeto cliente

    Argumentos:
        nombre (str): [nombre]
        apellido (str): [apellido]
        
    """

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular del objeto cliente.
        """
        return reverse('clientes:detalle', kwargs={'pk': self.id})

    def get_absolute_url_mod(self):
        return reverse('clientes:modificar', kwargs={"pk": self.id})


    def get_absolute_url_activar(self):
        return reverse('clientes:activar', kwargs={"pk": self.pk})
