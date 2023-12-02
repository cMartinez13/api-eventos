from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views import generic
from .models import Coordinador
from django.urls import reverse_lazy

# Create your views here.


class CoordinadorListView(generic.ListView):
    queryset = Coordinador.objects.filter(activo=True)
    model = Coordinador
    fields = '__all__'
    context_object_name = 'coordinadores'
    template_name= 'coordinadores/listar_coordinador.html'

class CoordinadorUpdateView(generic.UpdateView):
    model = Coordinador
    fields = '__all__'
    template_name = 'coordinadores/modificar_coordinador.html'
    extra_context = {'titulo': 'Modificar Coordinador', 'mensaje_boton': 'MODIFICAR'}
    success_url = reverse_lazy('coordinadores:listar')

