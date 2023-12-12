from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from .models import ReservaServicio
from django.http import JsonResponse

# Create your views here.


def listado_reservas(request):
    reservas = ReservaServicio.objects.all()
    return render(request, 'listado_reservas.html', {'reservas': reservas})

class ReservasCreateView(generic.CreateView):    
    model = ReservaServicio
    fields = '__all__'
    template_name = 'reservas_servicios/modificar_reserva_servicio.html'
    extra_context = {'titulo': 'Realizar reserva de servicio', 'mensaje_boton': 'CREAR'}
    success_url = reverse_lazy('reserva_servicios:listar')


class ResevasUpdateView(generic.UpdateView):
    model = ReservaServicio
    fields = '__all__'
    template_name = 'reservas_servicios/modificar_reserva_servicio.html'
    extra_context = {'titulo': 'Modificar Reserva de Servicio',
                     'mensaje_boton': 'MODIFICAR'}
    success_url = reverse_lazy('reserva_servicios:listar')


class ReservasDeleteView(generic.DeleteView):
    model = ReservaServicio
    template_name = 'reservas_servicios/confirm_delete.html'
    extra_context = {'titulo': 'Eliminar Reserva de Servicio',
                     'mensaje_boton': 'ELIMINAR'}
    success_url = reverse_lazy('reserva_servicios:listar')

class ReservasListView(generic.ListView):
    queryset = ReservaServicio.objects.all()
    model = ReservaServicio
    fields = '__all__'
    context_object_name = 'reserva_servicios'
    template_name = 'reservas_servicios/listar_reserva_servicio.html'

def lista_reservas(request):
    reservas = ReservaServicio.objects.all()
    data = [{'id': reserva.id, 'nombre': reserva.nombre} for reserva in reservas]
    return JsonResponse(data, safe=False)

def detalle_reserva(request, id):
    reserva = get_object_or_404(ReservaServicio, id=id)
    data = {
        'id': reserva.id,
        'nombre': reserva.nombre,
    }
    return JsonResponse(data)
