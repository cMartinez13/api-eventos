from django.shortcuts import render
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
