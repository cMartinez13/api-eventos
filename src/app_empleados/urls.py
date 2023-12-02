from django.urls import path
from . import views

app_name = 'empleados'

urlpatterns = [    
    path('listar/', views.EmpleadoListView.as_view(), name='listar'),
    
]
