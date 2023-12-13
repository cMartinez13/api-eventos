from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy

from django.views import generic
from .models import Servicio

# Create your views here.


class ServicioCreateView(generic.CreateView):
    model = Servicio
    fields = '__all__'
    template_name = 'servicios/modificar_servicio.html'
    extra_context = {'titulo': 'Nuevo Servicio', 'mensaje_boton': 'Crear'}
    success_url = reverse_lazy('servicios:listar')


class ServicioListView(generic.ListView):
    queryset = Servicio.objects.all()
    model = Servicio
    fields = '__all__'
    context_object_name = 'servicios'
    template_name = 'servicios/listar_servicio.html'


class ServicioDetailView(generic.DetailView):
    model = Servicio
    fields = '__all__'
    context_object_name = 'servicio'
    template_name = 'servicios/detalle_servicio.html'


class ServicioUpdateView(generic.UpdateView):
    model = Servicio
    fields = '__all__'
    template_name = 'servicios/modificar_servicio.html'
    extra_context = {'titulo': 'Modificar Servicio',
                     'mensaje_boton': 'MODIFICAR'}
    success_url = reverse_lazy('servicios:listar')


def activar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    servicio.activo = True
    servicio.save()
    messages.success(
        request, F"El Servicio {servicio.nombre}  ha sido activado exitosamente.")
    return redirect('/servicios/listar/')


def desactivar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    servicio.activo = False
    servicio.save()
    messages.success(
        request, F"El Servicio {servicio.nombre}  ha sido desactivado exitosamente.")
    return redirect('/servicios/listar/')
