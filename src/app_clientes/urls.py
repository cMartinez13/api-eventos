from django.urls import path
from . import views
# from .views import desactivar_cliente

app_name = 'clientes'

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('nuevo/', views.ClienteCreateView.as_view(), name='crear'),
    path('listar/', views.ClienteListView.as_view(), name='listar'),
    path('detalle/<int:pk>/', views.ClienteDetailView.as_view(), name='detalle'),
    path('modificar/<int:pk>/', views.ClienteUpdateView.as_view(), name='modificar'),
    path('desactivar/<int:pk>/', views.ClienteDesactivateView.as_view(), name='desactivar'),
    path('activar/<int:pk>/', views.activar_cliente, name='activar'),
    # path('eliminar/<int:pk>/', views.ClienteDeleteView.as_view(), name='eliminar'),
]

