from django.urls import path
from . import views

app_name = 'servicios'


urlpatterns = [
    path('nuevo/', views.ServicioCreateView.as_view(), name='nuevo'),
    path('activar/<int:pk>/', views.activar_servicio, name='activar'),
    path('listar/', views.ServicioListView.as_view(), name='listar'),
    path('detalle/<int:pk>/', views.ServicioDetailView.as_view(), name='detalle'),
    path('desactivar/<int:pk>/', views.desactivar_servicio, name='desactivar'),
    path('modificar/<int:pk>/', views.ServicioUpdateView.as_view(), name='modificar'),
]
