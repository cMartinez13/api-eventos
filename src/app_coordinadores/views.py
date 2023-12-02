from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views import generic
from .models import Coordinador
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render



# Create your views here.

class CoordinadorCreateView(generic.CreateView):
    model = Coordinador
    fields = '__all__'
    template_name = 'coordinadores/crear_coordinadores.html'
    success_url = reverse_lazy('coordinadores:listar')

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

# class CoordinadorDeleteView(generic.UpdateView):
#     model = Coordinador
#     fields = '__all__'
#     template_name = 'coordinadores/modificar.html'
#     extra_context = {'titulo': 'Modificar Coordinador', 'mensaje_boton': 'ELIMINAR'}
#     success_url = reverse_lazy('coordinadores:listar')



def activar_coordinador(request, id):
    coordinador = get_object_or_404(Coordinador, id=id)

    coordinador.activo = True
    coordinador.save()

    message = "El coordinador ha sido activado exitosamente."
    return render(request, 'activar_coordinador.html', {'message': message})