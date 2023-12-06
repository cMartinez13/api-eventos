
from django.urls import path
from . import views
# from .views import ListaEmpleados, DetalleEmpleado


app_name = 'api'

urlpatterns = [
    path('empleados/', views.ListaEmpleados.as_view(), name='lista_empleados'),
    path('empleados/<int:pk>/', views.DetalleEmpleado.as_view(), name='detalle_empleado'),

]
