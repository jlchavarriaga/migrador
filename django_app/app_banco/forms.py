# app_banco/forms.py

from django import forms
from .models import Cliente, Cuenta

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        # fields = '__all__'
        fields = ['nombres_cliente', 'apellidos_cliente', 'institucion', 'direccion_cliente', 'tipo_cliente', 'dui_cliente', 'fecha_nacimiento_cliente']
        widgets = {
            'fecha_nacimiento_cliente': forms.DateInput(attrs={'type': 'date'}),  # Selector de fecha
        }

class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        #fields = '__all__'
        fields = ['cliente', 'tipo_cuenta', 'saldo_cuenta', 'fecha_creacion_cuenta', 'saldo_inicial_cuenta']
        widgets = {
            'fecha_creacion_cuenta': forms.DateInput(attrs={'type': 'date'}),
        }