from django import forms
from datetime import date
from .models import Heroe

class HeroeForm(forms.ModelForm):
    class Meta:
        model = Heroe
        fields = '__all__'
        widgets = {
            'sexo': forms.Select(attrs=None, choices=[('M', 'Masculino'), ('F', 'Femenino')]),
            'fecha_registro': forms.DateInput(attrs={"type": "date"}),
        }
