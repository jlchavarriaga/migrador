# nombre_de_tu_app/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib import messages
import os
from .management.commands.export_transactions import Command as ExportCommand
from .models import Cliente, Cuenta, Transaccion
from .forms import ClienteForm, CuentaForm
import tempfile


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


@login_required
def cargar_transacciones(request):
    if request.method == 'POST' and request.FILES.get('file'):
        # Guardar temporalmente el archivo
        file = request.FILES['file']
        file_path = default_storage.save(f'temp/{file.name}', ContentFile(file.read()))

        # Ejecutar el proceso batch para cargar el archivo
        try:
            from .management.commands.load_transactions import Command
            command = Command()
            command.handle(file_path=file_path)
            messages.success(request, "Transacciones cargadas exitosamente.")
        except Exception as e:
            messages.error(request, f"Error al cargar las transacciones: {e}")

        # Eliminar el archivo temporal
        os.remove(file_path)

        return redirect('cargar_transacciones')

    return render(request, 'cargar_transacciones.html')


@login_required
def descargar_transacciones(request):
    # Crear un archivo temporal para la exportación
    with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as temp_file:
        file_path = temp_file.name

    # Ejecutar el proceso batch de exportación y generar el archivo
    export_command = ExportCommand()
    export_command.handle(file_path=file_path)

    # Enviar el archivo como respuesta para la descarga
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="transacciones_exportadas.xlsx"'

    # Borrar el archivo temporal después de enviar la respuesta
    os.remove(file_path)

    return response

@login_required
def transacciones_por_cuenta(request, cuenta_id):
    cuenta = get_object_or_404(Cuenta, id=cuenta_id)
    transacciones = Transaccion.objects.filter(cuenta=cuenta)

    context = {
        'cuenta': cuenta,
        'transacciones': transacciones
    }
    return render(request, 'transacciones_cuenta.html', context)
