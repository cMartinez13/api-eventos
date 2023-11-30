from django import forms
from .models import Coordinadores

class CoordinadoresForm(forms.ModelForm):
    class Meta:
        model = Coordinadores
        fields = ['nombre', 'apellido']
    
