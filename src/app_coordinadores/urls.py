from . import views
from django.urls import path
from .views import activar_coordinador

# NAME SPACE de la url de la app.
app_name = "coordinadores"

urlpatterns = [

    path('listar/', views.CoordinadorListView.as_view(), name='listar'),
    path('modificar/<int:pk>/',
         views.CoordinadorUpdateView.as_view(), name='modificar'),
    path('nuevo/', views.CoordinadorCreateView.as_view(), name='nuevo'),
    # path('desactivar/<int:pk>/',
    #      views.CoordinadorDesactivateView.as_view(), name='desactivar'),
    path('desactivar/<int:pk>/', views.desactivar_coordinador, name='desactivar'),
    path('activar/<int:pk>/', views.activar_coordinador, name='activar'),
]
