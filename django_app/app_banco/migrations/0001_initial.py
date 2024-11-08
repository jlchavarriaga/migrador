# Generated by Django 5.1.2 on 2024-11-04 16:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres_cliente', models.CharField(max_length=255)),
                ('apellidos_cliente', models.CharField(max_length=255)),
                ('tipo_cliente', models.CharField(max_length=50)),
                ('direccion_cliente', models.CharField(max_length=255)),
                ('dui_cliente', models.CharField(max_length=10)),
                ('fecha_nacimiento_cliente', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_institucion', models.CharField(max_length=255)),
                ('fecha_creacion_institucion', models.DateField()),
                ('descripcion_institucion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_cuenta', models.CharField(max_length=50)),
                ('saldo_cuenta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_creacion_cuenta', models.DateField()),
                ('saldo_inicial_cuenta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_banco.cliente')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='institucion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_banco.institucion'),
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_transaccion', models.TextField()),
                ('fecha_posteo_transaccion', models.DateField()),
                ('tipo_transaccion', models.CharField(max_length=50)),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_banco.cuenta')),
            ],
        ),
    ]
