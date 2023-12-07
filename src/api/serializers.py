
from rest_framework import serializers
from app_empleados.models import Empleado


class EmpleadoSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['id', 'nombre']


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'


class CoordinadorSerializerList(serializers.ModelSerializer):
    pass


class CoordinadorSerializer(serializers.ModelSerializer):
    pass
