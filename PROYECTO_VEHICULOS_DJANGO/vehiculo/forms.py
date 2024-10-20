from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    MARCAS_CHOICES = [
        ('Fiat', 'Fiat'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
        ('Chevrolet', 'Chevrolet'),
    ]

    CATEGORIAS_CHOICES = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    ]

    marca = forms.ChoiceField(choices=MARCAS_CHOICES, initial='Ford')
    categoria = forms.ChoiceField(choices=CATEGORIAS_CHOICES, initial='Particular')

    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']