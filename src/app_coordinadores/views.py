from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Coordinador


# Create your views here.

class CoordinadorCreateView(generic.CreateView):
    model = Coordinador
    fields = '__all__'
    template_name = 'coordinadores/crear_coordinadores.html'
    extra_context = {'titulo': 'Alta de Coordinador', 'mensaje_boton': 'CREAR'}
    success_url = reverse_lazy('coordinadores:listar')


class CoordinadorListView(generic.ListView):
    queryset = Coordinador.objects.all()
    model = Coordinador
    fields = '__all__'
    context_object_name = 'coordinadores'
    template_name = 'coordinadores/listar_coordinador.html'


class CoordinadorUpdateView(generic.UpdateView):
    queryset = Coordinador.objects.filter(activo=True)
    model = Coordinador
    fields = '__all__'
    template_name = 'coordinadores/crear_coordinadores.html'
    extra_context = {'titulo': 'Modificar Coordinador',
                     'mensaje_boton': 'MODIFICAR'}
    success_url = reverse_lazy('coordinadores:listar')


def activar_coordinador(request, pk):
    coordinador = get_object_or_404(Coordinador, pk=pk)

    coordinador.activo = True
    coordinador.save()

    message = "El coordinador ha sido activado exitosamente."
    return redirect('coordinadores:listar')


def desactivar_coordinador(request, pk):
    coordinador = get_object_or_404(Coordinador, pk=pk)

    coordinador.activo = False
    coordinador.save()

    message = "El coordinador ha sido desactivado."
    return redirect('coordinadores:listar')
