from django.contrib import admin
from .models import Empleado

# Register your models here.
# admin.site.register(Empleado)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['apellido', 'nombre', 'legajo', 'activo']
    list_filter = ['apellido', 'nombre', 'legajo', 'activo']
    search_fields = ['apellido', 'nombre', 'legajo', 'activo']
    ordering = ['apellido', 'nombre', 'legajo', 'activo']