from django.contrib import admin
from .models import Carro, Repuestos, Inventario, Empleados, Usuario, Cliente, Venta, Detalles_Venta, Comisiones, Departamentos, Pagos, Cotizacion, Cotizacion_Detalle, Compra_Carro, Compra_Repuesto, Proveedor, Bitacora_Alertas, Historial_Cambio, Cambios_Salarios

admin.site.register(Carro)
admin.site.register(Repuestos)