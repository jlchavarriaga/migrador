# nombre_de_tu_app/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Cliente, Cuenta
from .forms import ClienteForm, CuentaForm
from django.contrib.auth.decorators import login_required


# CRUD para Cliente
@login_required
def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/cliente_list.html', {'clientes': clientes})

@login_required
def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'clientes/cliente_detail.html', {'cliente': cliente})

@login_required
def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cliente_form.html', {'form': form})

@login_required
def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/cliente_form.html', {'form': form})

@login_required
def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()  # Esto eliminará en cascada las cuentas asociadas
    return redirect('cliente_list')


# CRUD para Cuenta
@login_required
def cuenta_list(request):
    cuentas = Cuenta.objects.all()
    return render(request, 'cuentas/cuenta_list.html', {'cuentas': cuentas})

@login_required
def cuenta_detail(request, pk):
    cuenta = get_object_or_404(Cuenta, pk=pk)
    return render(request, 'cuentas/cuenta_detail.html', {'cuenta': cuenta})

@login_required
def cuenta_create(request):
    if request.method == 'POST':
        form = CuentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cuenta_list')
    else:
        form = CuentaForm()
    return render(request, 'cuentas/cuenta_form.html', {'form': form})

@login_required
def cuenta_update(request, pk):
    cuenta = get_object_or_404(Cuenta, pk=pk)
    if request.method == 'POST':
        form = CuentaForm(request.POST, instance=cuenta)
        if form.is_valid():
            form.save()
            return redirect('cuenta_list')
    else:
        form = CuentaForm(instance=cuenta)
    return render(request, 'cuentas/cuenta_form.html', {'form': form})

@login_required
def cuenta_delete(request, pk):
    cuenta = get_object_or_404(Cuenta, pk=pk)
    cuenta.delete()  # Eliminará la cuenta seleccionada
    return redirect('cuenta_list')
