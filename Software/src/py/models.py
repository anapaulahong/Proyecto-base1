from django.db import models

class Carro(models.Model):
    CarroID = models.IntegerField(primary_key=True)
    Marca = models.CharField(max_length=100)
    Modelo = models.CharField(max_length=100)
    Transmision = models.CharField(max_length=100)

class Repuestos(models.Model):
    RepuestoID = models.IntegerField(primary_key=True)
    CarroID = models.IntegerField()
    Nombre = models.CharField(max_length=100)
    Categoria = models.CharField(max_length=100)
    Precio_Unitario = models.DecimalField(max_digits=10, decimal_places=2)
    Carro = models.ForeignKey(Carro, on_delete=models.CASCADE)

class Inventario(models.Model):
    CarroID = models.IntegerField()
    RepuestoID = models.IntegerField()
    Existencia = models.IntegerField()
    Cantidad_Minima = models.IntegerField()
    Carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    Repuestos = models.ForeignKey(Repuestos, on_delete=models.CASCADE)

class Empleados(models.Model):
    EmpleadoDPI = models.IntegerField(primary_key=True)
    Nombres = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    Sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    departamento_id = models.IntegerField()
    departamento = models.ForeignKey('Departamentos', on_delete=models.CASCADE)

class Usuario(models.Model):
    EmpleadoDPI = models.IntegerField()
    Usuario = models.CharField(max_length=100)
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)

class Cliente(models.Model):
    NIT = models.IntegerField(primary_key=True)
    Nombre_Cliente = models.CharField(max_length=100)
    Contacto = models.CharField(max_length=100)
    Tipo = models.CharField(max_length=100)

class Venta(models.Model):
    Numero_Orden = models.IntegerField(primary_key=True)
    CajaDPI = models.IntegerField()
    BodegaDPI = models.IntegerField()
    NIT = models.IntegerField()
    Total = models.DecimalField(max_digits=10, decimal_places=2)
    MetodoPago = models.CharField(max_length=100)
    Fecha = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Detalles_Venta(models.Model):
    Numero_Orden = models.IntegerField()
    RepuestoID = models.IntegerField()
    Cantidad = models.IntegerField()
    Rebaja = models.DecimalField(max_digits=10, decimal_places=2)
    SubTotal = models.DecimalField(max_digits=10, decimal_places=2)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    repuesto = models.ForeignKey(Repuestos, on_delete=models.CASCADE)

class Comisiones(models.Model):
    ComisionID = models.IntegerField(primary_key=True)
    EmpleadoDPI = models.IntegerField()
    NumOrden = models.IntegerField()
    Tipo = models.CharField(max_length=100)
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)

class Departamentos(models.Model):
    DepaID = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=100)

class Pagos(models.Model):
    MetodoPagoID = models.IntegerField(primary_key=True)
    MetodoPago = models.CharField(max_length=100)
    Usuario = models.CharField(max_length=100)
    EmpleadoDPI = models.IntegerField()
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)

class Cotizacion(models.Model):
    CotizacionID = models.IntegerField(primary_key=True)
    VendedorID = models.IntegerField()
    Total = models.DecimalField(max_digits=10, decimal_places=2)
    Fecha = models.DateTimeField()
    vendedor = models.ForeignKey(Empleados, on_delete=models.CASCADE)

class Cotizacion_Detalle(models.Model):
    CotizacionDetalleID = models.IntegerField(primary_key=True)
    CotizacionID = models.IntegerField()
    RepuestoID = models.IntegerField()
    Cantidad = models.IntegerField()
    Precio_Unitario = models.DecimalField(max_digits=10, decimal_places=2)
    Precio_Total = models.DecimalField(max_digits=10, decimal_places=2)
    Numero_Linea = models.IntegerField()
    cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    repuesto = models.ForeignKey(Repuestos, on_delete=models.CASCADE)

class Compra_Carro(models.Model):
    Fecha = models.DateTimeField()
    Cantidad = models.IntegerField()
    CarroID = models.IntegerField()
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)

class Compra_Repuesto(models.Model):
    CompraRepuestoID = models.IntegerField(primary_key=True)
    RepuestoID = models.IntegerField()
    Costo = models.DecimalField(max_digits=10, decimal_places=2)
    ProveedorID = models.IntegerField()
    repuesto = models.ForeignKey(Repuestos, on_delete=models.CASCADE)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)

class Proveedor(models.Model):
    ProveedorID = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=100)
    Contacto = models.CharField(max_length=100)

class Bitacora_Alertas(models.Model):
    AlertaID = models.IntegerField(primary_key=True)
    RepuestoID = models.IntegerField()
    Fecha = models.DateTimeField()
    repuesto = models.ForeignKey(Repuestos, on_delete=models.CASCADE)

class Historial_Cambio(models.Model):
    CambioID = models.IntegerField(primary_key=True)
    Tipo_Cambio = models.CharField(max_length=100)
    Tabla_Afectada = models.CharField(max_length=100)
    ID_Registro = models.IntegerField()
    Usuario = models.CharField(max_length=100)
    Fecha = models.DateTimeField()
    Comentario = models.TextField()

class Cambios_Salarios(models.Model):
    Cambio_SalarioID = models.IntegerField(primary_key=True)
    EmpleadoDPI = models.IntegerField()
    Fecha_Cambio = models.DateTimeField()
    Salario_Anterior = models.DecimalField(max_digits=10, decimal_places=2)
    Salario_Nuevo = models.DecimalField(max_digits=10, decimal_places=2)
    Motivo = models.CharField(max_length=100)
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)

