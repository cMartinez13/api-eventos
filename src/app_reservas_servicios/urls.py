from django.urls import path
from . import views


app_name = 'reserva_servicios'

urlpatterns = [
    path('listado/', views.listado_reservas, name='listado_reservas'),
    path('eliminar/<int:pk>/',
         views.ReservasDeleteView.as_view(), name='eliminar'),
]
