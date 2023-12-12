from django.urls import path
from . import views



app_name = 'reserva'

urlpatterns = [
    path('', views.home, name='home'),
    
    ]
