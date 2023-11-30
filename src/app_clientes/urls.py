from django.urls import path
from .views import registrar_cliente, desactivar_cliente

urlpatterns = [
    path('clientes/registrar/', registrar_cliente, name='registrar_cliente'),
    path('clientes/desactivar/<int:id>/', desactivar_cliente, name='desactivar_cliente'),
    
]
