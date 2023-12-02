from django.shortcuts import render
from django.views import generic
from .models import Empleado

# Create your views here.
class EmpleadoCreateView(generic.CreateView):
    model: Empleado
    fields = '__all__'
    #template_name = ''

class EmpleadoListView(generic.ListView):
    queryset = Empleado.objects.filter(activo=True)
    model = Empleado
    fields = '__all__'
    context_object_name = 'empleados'
    template_name= 'empleados/listar_empleado.html'

