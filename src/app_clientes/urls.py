from django.urls import path
from .views import registrar_cliente

urlpatterns = [
    path('clientes/registrar/', registrar_cliente, name='registrar_cliente'),
    
]
