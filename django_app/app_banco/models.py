from django.db import models

class Institucion(models.Model):
    nombre_institucion = models.CharField(max_length=255)
    fecha_creacion_institucion = models.DateField()
    descripcion_institucion = models.TextField()
    def __str__(self):
        return self.nombre_institucion

class Cliente(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    nombres_cliente = models.CharField(max_length=255)
    apellidos_cliente = models.CharField(max_length=255)
    tipo_cliente = models.CharField(max_length=50)
    direccion_cliente = models.CharField(max_length=255)
    dui_cliente = models.CharField(max_length=10)
    fecha_nacimiento_cliente = models.DateField()
    def __str__(self):
        return f"{self.nombres_cliente} {self.apellidos_cliente}"

class Cuenta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_cuenta = models.CharField(max_length=50)
    saldo_cuenta = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion_cuenta = models.DateField()
    saldo_inicial_cuenta = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.cliente.nombres_cliente} {self.cliente.apellidos_cliente} - {self.tipo_cuenta} : {self.saldo_cuenta}"

class Transaccion(models.Model):
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    descripcion_transaccion = models.TextField()
    fecha_posteo_transaccion = models.DateField()
    tipo_transaccion = models.CharField(max_length=50)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        cliente_nombre = f"{self.cuenta.cliente.nombres_cliente} {self.cuenta.cliente.apellidos_cliente}" if self.cuenta and self.cuenta.cliente else "Cliente desconocido"
        return f"{cliente_nombre} - {self.cuenta.tipo_cuenta if self.cuenta else 'Cuenta desconocida'}: {self.descripcion_transaccion} - {self.monto}"