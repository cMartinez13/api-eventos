from django.urls import path
from . import views
from .views import lista_reservas, detalle_reserva

app_name = 'reserva_servicios'

urlpatterns = [

    path('eliminar/<int:pk>/', views.ReservasDeleteView.as_view(), name='eliminar'),
    path('nuevo/', views.ReservasCreateView.as_view(), name='nuevo'),
    path('modificar/<int:pk>/', views.ResevasUpdateView.as_view(), name='modificar'),
    path('listar/', views.ReservasListView.as_view(), name='listar'),
    # Falta detalle.
]
