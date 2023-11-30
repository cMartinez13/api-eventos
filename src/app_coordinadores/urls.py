from . import views
from django.urls import path

# NAME SPACE de la url de la app.
app_name = "coordinador"

urlpatterns = [

    path('modificar/<int:pk>/',
         views.CoordinadorUpdateView.as_view(), name='modificar'),

]
