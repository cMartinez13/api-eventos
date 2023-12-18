from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from .models import ReservaServicio
from app_clientes.models import Cliente
from app_coordinadores.models import Coordinador
from app_empleados.models import Empleado
from app_servicio.models import Servicio


# Create your views here.


class ReservasCreateView(generic.CreateView):
    model = ReservaServicio
    fields = '__all__'
    template_name = 'reservas_servicios/crear_reserva_servicio.html'
    clientes = Cliente.objects.filter(activo=True)
    empleados = Empleado.objects.filter(activo=True)
    servicios = Servicio.objects.filter(activo=True)
    coordinadores = Coordinador.objects.filter(activo=True)
    extra_context = {'titulo': 'Nueva Reserva ',
                     'mensaje_boton': 'CREAR', 'clientes': clientes, 'empleados': empleados, 'servicios': servicios, 'coordinadores': coordinadores}
    success_url = reverse_lazy('reserva_servicios:listar')


class ResevasUpdateView(generic.UpdateView):
    model = ReservaServicio
    fields = '__all__'
    template_name = 'reservas_servicios/modificar_reserva_servicio.html'
    clientes = Cliente.objects.filter(activo=True)
    empleados = Empleado.objects.filter(activo=True)
    servicios = Servicio.objects.filter(activo=True)
    coordinadores = Coordinador.objects.filter(activo=True)
    extra_context = {'titulo': 'Modificar Reserva ',
                     'mensaje_boton': 'MODIFICAR', 'clientes': clientes, 'empleados': empleados, 'servicios': servicios, 'coordinadores': coordinadores}
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
