# en views.py
from django.shortcuts import get_object_or_404, render
from .models import Coordinador

def activar_coordinador(request, id):
    coordinador = get_object_or_404(Coordinador, id=id)

    
    coordinador.activo = True
    coordinador.save()

    
    message = "El coordinador ha sido activado exitosamente."
    return render(request, 'activar_coordinador.html', {'message': message})
