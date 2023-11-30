from django.shortcuts import render, redirect
from .form import CoordinadorForm

def registrar_coordinador(request):
    if request.method == 'POST':
        form = CoordinadorForm(request.POST)
    if form.is_valid():
            form.save()
            return redirect('lista_coordinadores')  # Redirige a la lista de coordinadores o a donde desees
    else:
        form = CoordinadorForm()

    return render(request, 'registrar_coordinador.html', {'form': form})
