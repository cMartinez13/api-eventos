from django.urls import path
from . import views

app_name = 'servicios'


urlpatterns = [
    path('nuevo/', views.ServicioCreateView.as_view(), name='nuevo'),

]
