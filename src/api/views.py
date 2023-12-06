from django.shortcuts import render
from rest_framework import generics
from app_empleados.models import Empleado
from .serializers import EmpleadoSerializer

# Create your views here.


class ListaEmpleados(generics.ListAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class DetalleEmpleado(generics.RetrieveAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
