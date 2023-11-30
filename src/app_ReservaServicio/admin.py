from django.contrib import admin
from .models import ReservaServicio

# Register your models here.
@admin.register(ReservaServicio)
class ReservaServicioAdmin(admin.ModelAdmin):
    list_display = ('cliente','servicio', 'fecha_reserva', 'fecha_servicio', 'empleado', 'coordinador' )
    search_fields = ('cliente', 'servicio', 'fecha_reserva')
    
