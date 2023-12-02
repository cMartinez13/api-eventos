from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('nuevo/', views.ClienteCreateView.as_view(), name='crear'),
    path('listar/', views.ClienteListView.as_view(), name='listar'),
    path('detalle/<int:pk>/', views.ClienteDetailView.as_view(), name='detalle'),
    path('modificar/<int:pk>/', views.ClienteUpdateView.as_view(), name='modificar'),
    # path('eliminar/<int:pk>/', views.ClienteDeleteView.as_view(), name='eliminar'),
]

