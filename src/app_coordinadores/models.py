from django.db import models

# Create your models here.
class Coordinador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.IntegerField()
    fecha_alta = models.DateTimeField()
    activo = models.BooleanField(default=True) 