from django.urls import path
from . import views

app_name = 'empleados'

urlpatterns = [
    path('listar/', views.EmpleadoListView.as_view(), name='listar'),
    path('nuevo/', views.EmpleadoCreateView.as_view(), name='nuevo'),
    path('modificar/<int:pk>/', views.EmpleadoUpdateView.as_view(), name='modificar'),
    path('desactivar/<int:pk>/', views.desactivar_empleado, name='desactivar'),
    path('activar/<int:pk>/', views.activar_empleado, name='activar'),
]
