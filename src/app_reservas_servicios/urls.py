from django.urls import path
from . import views


app_name = 'reserva_servicios'

urlpatterns = [
   path('reservas/listado/', views.listado_reservas, name='listado_reservas'),

]