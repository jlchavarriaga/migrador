# app_banco/management/commands/export_transactions.py

import pandas as pd
from django.core.management.base import BaseCommand
from app_banco.models import Transaccion

class Command(BaseCommand):
    help = 'Exporta todos los registros de la tabla Transaccion a un archivo Excel'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Ruta donde se guardará el archivo Excel")

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            transacciones = Transaccion.objects.all().values(
                'cuenta__id', 'cuenta__cliente__nombres_cliente', 'cuenta__cliente__apellidos_cliente',
                'descripcion_transaccion', 'fecha_posteo_transaccion', 'tipo_transaccion', 'monto'
            )

            df = pd.DataFrame(transacciones)

            df.rename(columns={
                'cuenta__id': 'ID Cuenta',
                'cuenta__cliente__nombres_cliente': 'Nombre Cliente',
                'cuenta__cliente__apellidos_cliente': 'Apellido Cliente',
                'descripcion_transaccion': 'Descripción',
                'fecha_posteo_transaccion': 'Fecha de Posteo',
                'tipo_transaccion': 'Tipo de Transacción',
                'monto': 'Monto'
            }, inplace=True)

            df.to_excel(file_path, index=False)
            self.stdout.write(self.style.SUCCESS(f"Exportación completada exitosamente en {file_path}"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error al exportar los datos: {e}"))
