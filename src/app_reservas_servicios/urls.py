from django.urls import path
from . import views

app_name = 'reserva_servicios'

urlpatterns = [

    path('nuevo/', views.ReservasCreateView.as_view(), name='nuevo'),
    path('listar/', views.ReservasListView.as_view(), name='listar'),
    path('modificar/<int:pk>/', views.ResevasUpdateView.as_view(), name='modificar'),
    path('eliminar/<int:pk>/', views.ReservasDeleteView.as_view(), name='eliminar'),

    # Falta detalle.
]
