from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from .models import Cliente


class ClienteCreateView(generic.CreateView):
    model = Cliente
    fields = '__all__'
    template_name = 'clientes/modificar_cliente.html'
    extra_context = {'titulo': 'Alta de Cliente', 'mensaje_boton': 'CREAR'}
    success_url = reverse_lazy('clientes:listar')


class ClienteListView(generic.ListView):
    queryset = Cliente.objects.all()
    model = Cliente
    fields = '__all__'
    context_object_name = 'clientes'
    template_name = 'clientes/listar_cliente.html'


class ClienteDetailView(generic.DetailView):
    model = Cliente
    fields = '__all__'
    context_object_name = 'cliente'
    template_name = 'clientes/detalle_cliente.html'


class ClienteUpdateView(generic.UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = 'clientes/modificar_cliente.html'
    extra_context = {'titulo': 'Modificar Cliente',
                     'mensaje_boton': 'MODIFICAR'}
    success_url = reverse_lazy('clientes:listar')


def activar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.activo = True
    cliente.save()
    messages.success(
        request, F"El cliente {cliente.apellido} {cliente.nombre} ha sido activado exitosamente.")
    return redirect('/clientes/listar/')


def desactivar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    cliente.activo = False
    cliente.save()
    messages.info(
        request, F"El cliente {cliente.apellido} {cliente.nombre} ha sido desactivado.")
    return redirect('clientes:listar')
