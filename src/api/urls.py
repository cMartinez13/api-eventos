
from django.urls import path
from . import views
from .views import ListaEmpleados, DetalleEmpleado


app_name = 'api'

urlpatterns = [
    path('api/empleados/', ListaEmpleados.as_view(), name='lista_empleados'),
    path('api/empleados/<int:pk>/', DetalleEmpleado.as_view(), name='detalle_empleado'),

]
