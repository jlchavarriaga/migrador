# app_banco/forms.py

from django import forms
from .models import Cliente, Cuenta

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = '__all__'
