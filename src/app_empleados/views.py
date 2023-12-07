from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Empleado

# Create your views here.


class EmpleadoCreateView(generic.CreateView):
    model = Empleado
    fields = '__all__'
    template_name = 'empleados/crear_empleado.html'
    extra_context = {'titulo': 'Alta de Empleado', 'mensaje_boton': 'CREAR'}
    success_url = reverse_lazy('empleados:listar')


class EmpleadoListView(generic.ListView):
    # queryset = Empleado.objects.filter(activo=True)
    queryset = Empleado.objects.all()
    model = Empleado
    fields = '__all__'
    context_object_name = 'empleados'
    template_name = 'empleados/listar_empleado.html'
