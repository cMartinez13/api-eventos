from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
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
    queryset = Empleado.objects.all()
    model = Empleado
    fields = '__all__'
    context_object_name = 'empleados'
    template_name = 'empleados/listar_empleado.html'


class EmpleadoDetailView(generic.DetailView):
    model = Empleado
    fields = '__all__'
    context_object_name = 'empleado'
    template_name = 'empleados/detalle_empleado.html'


class EmpleadoUpdateView(generic.UpdateView):
    model = Empleado
    fields = '__all__'
    template_name = 'empleados/modificar_empleado.html'
    extra_context = {'titulo': 'Modificar Empleado',
                     'mensaje_boton': 'MODIFICAR'}
    success_url = reverse_lazy('empleados:listar')


def activar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    empleado.activo = True
    empleado.save()
    messages.success(
        request, F"El Empleado {empleado.nombre}  ha sido activado exitosamente.")
    return redirect('/empleados/listar/')


def desactivar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    empleado.activo = False
    empleado.save()
    messages.success(
        request, F"El Empleado {empleado.nombre}  ha sido desactivado exitosamente.")
    return redirect('/empleados/listar/')
