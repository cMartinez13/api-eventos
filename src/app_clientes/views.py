from django.shortcuts import render, redirect
from .form import ClienteForm

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()

    return render(request, 'registrar_cliente.html', {'form': form})
