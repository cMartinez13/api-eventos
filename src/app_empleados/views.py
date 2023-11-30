from django.shortcuts import render
from django.views import generic
from .models import Empleado

# Create your views here.
class EmpleadoCreateView(generic.CreateView):
    model: Empleado
    fields = '__all__'
    #template_name = ''


