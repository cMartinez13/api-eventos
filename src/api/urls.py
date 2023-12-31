
from django.urls import path
from . import views


app_name = 'api'

urlpatterns = [
    path('home/', views.home_api, name='home_api'),
    path('empleados/', views.ListaEmpleados.as_view(), name='lista_empleados'),
    path('empleados/<int:pk>/', views.DetalleEmpleado.as_view(),
         name='detalle_empleado'),
    path('coordinadores/', views.ListaCoordinadores.as_view(),
         name='lista_coordinadores'),
    path('coordinadores/<int:pk>/', views.DetalleCoordinadores.as_view(),
         name='detalle_coordinadores'),
    path('servicios/', views.ListaServicios.as_view(), name='lista_servicios'),
    path('servicios/<int:pk>/', views.DetalleServicios.as_view(),
         name='detalle_servicios'),
    path('reservas_servicios/', views.ListaReservaServicios.as_view(),
         name='lista_reservas_servicios'),
    path('reservas_servicios/<int:pk>/', views.DetalleReservaServicios.as_view(),
         name='detalle_reservas_servicios'),
    path('clientes/', views.ListaClientes.as_view(), name='lista_clientes'),
    path('clientes/<int:pk>/', views.DetalleClientes.as_view(),
         name='detalle_clientes'),

]
