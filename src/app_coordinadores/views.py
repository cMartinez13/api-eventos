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
