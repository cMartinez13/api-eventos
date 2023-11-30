from django.contrib import admin
from .models import ReservaServicio

# Register your models here.
@admin.register(ReservaServicio)
class ReservaServicio(admin.ModelAdmin):
    list_display = ['cliente', 'fecha_reserva', 'fecha_servicio', 'empleado']
    search_fields = ['cliente', 'servicio', 'fecha_reserva']
    
