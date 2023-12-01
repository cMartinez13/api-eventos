from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views import generic
from .models import Coordinador
from django.urls import reverse_lazy

# Create your views here.


class CoordinadorUpdateView(generic.UpdateView):
    model = Coordinador
    fields = ['nombre', 'apellido', 'documento']
    template_name = 'coordinadores/modificar.html'

    # success_url = reverse_lazy("coordinador:listar")


class CoordinadorListView(generic.ListView):
    model = Coordinador
    fields = '__all__'
    context_object_name = 'coordinador'
    template_name = 'coordinadores/lista.html'

# class CoordinadorDeleteView(generic.UpdateView):
#     model = Coordinador
#     fields = '__all__'
#     template_name = 'coordinadores/modificar.html'
#     extra_context = {'titulo': 'Modificar Coordinador', 'mensaje_boton': 'ELIMINAR'}
#     success_url = reverse_lazy('coordinadores:listar')

