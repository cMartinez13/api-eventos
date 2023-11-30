from django.db import models

class Coordinador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    activo = models.BooleanField(default=False)
    
