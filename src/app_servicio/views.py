from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy

from django.views import generic
from .models import Servicio

# Create your views here.


class ServicioCreateView(generic.CreateView):
    model = Servicio
    fields = '__all__'
    template_name = 'servicios/crear_servicios.html'
    extra_context = {'titulo': 'Nuevo Servicio', 'mensaje_boton': 'Crear'}
    success_url = reverse_lazy('servicio:listar')


def activar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    servicio.activo = True
    servicio.save()
    messages.success(
        request, F"El Servicio {servicio.nombre}  ha sido activado exitosamente.")
    return redirect('/servicios/listar/')
