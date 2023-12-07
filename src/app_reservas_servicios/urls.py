from django.urls import path
from . import views


app_name = 'reserva_servicios'

urlpatterns = [
    #path('listado/', views.listado_reservas, name='listado_reservas'),
    path('eliminar/<int:pk>/',
         views.ReservasDeleteView.as_view(), name='eliminar'),
    path('nuevo/', views.ReservasCreateView.as_view(), name='crear'),
    path('modificar/<int:pk>/', views.ResevasUpdateView.as_view(), name='modificar'),
    path('listar/', views.ReservasListView.as_view(), name='listar'),
]
