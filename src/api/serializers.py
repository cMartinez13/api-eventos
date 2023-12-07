
from rest_framework import serializers
from app_empleados.models import Empleado
from app_coordinadores.models import Coordinador
from app_servicio.models import Servicio


class EmpleadoSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['id', 'nombre']


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'


class CoordinadorSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Coordinador
        fields = ['id', 'nombre']


class CoordinadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinador
        fields = '__all__'


class ServicioSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['id', 'nombre']


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'
