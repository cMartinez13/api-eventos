from django.shortcuts import render
from rest_framework import generics
from app_empleados.models import Empleado
from app_coordinadores.models import Coordinador
from app_servicio.models import Servicio
from app_clientes.models import Cliente
from app_reservas_servicios.models import ReservaServicio
from .serializers import EmpleadoSerializer, EmpleadoSerializerList, CoordinadorSerializerList, CoordinadorSerializer
from .serializers import ReservaServicioSerializerList, ReservaServicioSerializer, ServicioSerializer, ServicioSerializerList
from .serializers import ClienteSerializerList, ClienteSerializer
# Create your views here.

# EMPLEADOS

def home_api(request):
    return render(request, 'home_api.html')

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

class ListaClientes(generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializerList


class DetalleClientes(generics.RetrieveAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
