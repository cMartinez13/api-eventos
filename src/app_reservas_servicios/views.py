from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from .models import ReservaServicio

# Create your views here.


def listado_reservas(request):
    reservas = ReservaServicio.objects.all()
    return render(request, 'listado_reservas.html', {'reservas': reservas})


class ResevasUpdateView(generic.UpdateView):
    model = ReservaServicio
    fields = '__all__'
    template_name = 'reservas_servicios/modificar_reserva_servicio.html'
    extra_context = {'titulo': 'Modificar Reserva de Servicio',
                     'mensaje_boton': 'MODIFICAR'}
    success_url = reverse_lazy('clientes:listar')


class ReservasDeleteView(generic.DeleteView):
    model = ReservaServicio
    template_name = 'reservas_servicios/confirm_delete.html'
    extra_context = {'titulo': 'Eliminar Reserva de Servicio',
                     'mensaje_boton': 'ELIMINAR'}
    success_url = reverse_lazy('clientes:listar')
