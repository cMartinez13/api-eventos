from django.shortcuts import render, redirect, get_object_or_404
from .form import ClienteForm
from .models import Cliente

def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()

    return render(request, 'registrar_cliente.html', {'form': form})


def desactivar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    cliente.activo = False
    cliente.save()

    message = "El cliente ha sido desactivado exitosamente."
    return render(request, 'desactivar_cliente.html', {'message': message})
