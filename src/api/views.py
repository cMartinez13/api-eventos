from django.shortcuts import render
from rest_framework import generics
from app_empleados.models import Empleado
from app_coordinadores.models import Coordinador
from .serializers import EmpleadoSerializer, EmpleadoSerializerList, CoordinadorSerializerList, CoordinadorSerializer

# Create your views here.


class ListaEmpleados(generics.ListAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializerList


class DetalleEmpleado(generics.RetrieveAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer


class ListaCoordinadores(generics.ListAPIView):
    queryset = Coordinador.objects.all()
    serializer_class = CoordinadorSerializerList


class DetalleCoordinadores(generics.ListAPIView):
    queryset = Coordinador.objects.all()
    serializer_class = CoordinadorSerializer
