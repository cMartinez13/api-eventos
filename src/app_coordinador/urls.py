from django.urls import path
from .views import activar_coordinador

urlpatterns = [
    path('coordinadores/activar/<int:id>/', activar_coordinador, name='activar_coordinador'),
    
]
