from django import forms
from .models import ReservaServicio


class ReservaServicioForm(forms.ModelForm):

    class Meta:
        model = ReservaServicio
        fields = ['fecha_reserva', 'fecha_servicio',
                  'cliente', 'servicio', 'empleado', 'coordinador']
        labels = {
            'fecha_reserva': 'Fecha de Reserva',
            'fecha_servicio': 'Fecha de Servicio',
            'cliente': 'Cliente',
            'servicio': 'Servicio',
            'empleado': 'Empleado',
            'coordinador': 'Coordinador',

        }
