from django.shortcuts import render
from rest_framework import generics
from app_empleados.models import Empleado
from app_coordinadores.models import Coordinador
from app_servicio.models import Servicio
from app_reservas_servicios.models import ReservaServicio
from .serializers import EmpleadoSerializer, EmpleadoSerializerList, CoordinadorSerializerList, CoordinadorSerializer
from .serializers import ReservaServicioSerializerList, ReservaServicioSerializer, ServicioSerializer, ServicioSerializerList

# Create your views here.

# EMPLEADOS


class ListaEmpleados(generics.ListAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializerList


class DetalleEmpleado(generics.RetrieveAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

# COORDINADORES


class ListaCoordinadores(generics.ListAPIView):
    queryset = Coordinador.objects.all()
    serializer_class = CoordinadorSerializerList


class DetalleCoordinadores(generics.RetrieveAPIView):
    queryset = Coordinador.objects.all()
    serializer_class = CoordinadorSerializer

# SERVICIOS


class ListaServicios(generics.ListAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializerList


class DetalleServicios(generics.RetrieveAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer


# Reserva Servicio

class ListaReservaServicios(generics.ListAPIView):
    queryset = ReservaServicio.objects.all()
    serializer_class = ReservaServicioSerializerList


class DetalleReservaServicios(generics.RetrieveAPIView):
    queryset = ReservaServicio.objects.all()
    serializer_class = ReservaServicioSerializer
