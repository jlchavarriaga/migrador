# app_banco/management/commands/load_transactions.py

import pandas as pd
from django.core.management.base import BaseCommand
from app_banco.models import Transaccion, Cuenta
from datetime import datetime
from django.db import transaction

class Command(BaseCommand):
    help = 'Carga un archivo Excel en la tabla Transaccion'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Ruta del archivo Excel a cargar")

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            data = pd.read_excel(file_path, engine='openpyxl')

            transacciones = []
            for index, row in data.iterrows():
                cuenta_id = row['cuenta_id']
                cuenta = Cuenta.objects.get(id=cuenta_id)

                transaccion = Transaccion(
                    cuenta=cuenta,
                    descripcion_transaccion=row['descripcion_transaccion'],
                    fecha_posteo_transaccion=datetime.strptime(row['fecha_posteo_transaccion'], '%Y-%m-%d').date(),
                    tipo_transaccion=row['tipo_transaccion'],
                    monto=row['monto']
                )
                transacciones.append(transaccion)

            batch_size = 1000
            with transaction.atomic():
                for i in range(0, len(transacciones), batch_size):
                    Transaccion.objects.bulk_create(transacciones[i:i+batch_size])

            self.stdout.write(self.style.SUCCESS("Carga completada exitosamente"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error al cargar el archivo: {e}"))
