from django.shortcuts import render
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
    queryset = Cliente.objects.filter(activo=True)
    model = Cliente
    fields = '__all__'
    context_object_name = 'clientes'
    template_name= 'clientes/listar_cliente.html'

class ClienteDetailView(generic.DetailView):
    model = Cliente
    fields = '__all__'
    context_object_name = 'cliente'
    template_name = 'clientes/detalle_cliente.html'

class ClienteUpdateView(generic.UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = 'clientes/modificar_cliente.html'
    extra_context = {'titulo': 'Modificar Cliente', 'mensaje_boton': 'MODIFICAR'}
    success_url = reverse_lazy('clientes:listar')

# class ClienteDeleteView(generic.UpdateView):
#     model = Cliente
#     fields = '__all__'
#     template_name = 'clientes/modificar_cliente.html'
#     extra_context = {'titulo': 'Modificar Cliente', 'mensaje_boton': 'ELIMINAR'}
#     success_url = reverse_lazy('clientes:listar')







