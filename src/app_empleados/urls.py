from django.urls import path
from . import views

app_name = 'empleados'

urlpatterns = [
    path('crear/', views.EmpleadoCreateView.as_view(), name='crear'),
   
]
