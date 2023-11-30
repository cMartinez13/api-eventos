from .form import CoordinadorForm
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


def registrar_coordinador(request):
    if request.method == 'POST':
        form = CoordinadorForm(request.POST)
    if form.is_valid():
        form.save()
        # Redirige a la lista de coordinadores o a donde desees
        return redirect('lista_coordinadores')
    else:
        form = CoordinadorForm()

    return render(request, 'registrar_coordinador.html', {'form': form})
