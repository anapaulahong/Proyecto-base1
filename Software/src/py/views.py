from django.shortcuts import render
from .models import Empleados
from .models import Carro
from .models import Repuestos
from .models import Inventario
from .models import Usuario
from .models import Cliente
from .models import Venta
from .models import Detalles_Venta
from .models import Comisiones
from .models import Departamentos
from .models import Pagos
from .models import Cotizacion
from .models import Cotizacion_Detalle
from .models import Compra_Carro
from .models import Compra_Repuesto
from .models import Proveedor
from .models import Bitacora_Alertas
from .models import Historial_Cambio
from .models import Cambios_Salarios

def lista_empleados(request):
    empleados = Empleados.objects.all()
    return render(request, 'empleados.html', {'empleados': empleados})

def lista_carros(request):
    carros = Carro.objects.all()
    return render(request, 'carros.html', {'carros': carros})

def lista_repuestos(request):
    repuestos = Repuestos.objects.all()
    return render(request, 'repuestos.html', {'repuestos': repuestos})

def lista_inventario(request):
    inventario = Inventario.objects.all()
    return render(request, 'inventario.html', {'inventario': inventario})

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas.html', {'ventas': ventas})

def detalles_venta(request):
    detalles_venta = Detalles_Venta.objects.all()
    return render(request, 'detalles_venta.html', {'detalles_venta': detalles_venta})

def lista_comisiones(request):
    comisiones = Comisiones.objects.all()
    return render(request, 'comisiones.html', {'comisiones': comisiones})

def lista_departamentos(request):
    departamentos = Departamentos.objects.all()
    return render(request, 'departamentos.html', {'departamentos': departamentos})

def lista_pagos(request):
    pagos = Pagos.objects.all()
    return render(request, 'pagos.html', {'pagos': pagos})

def lista_cotizaciones(request):
    cotizaciones = Cotizacion.objects.all()
    return render(request, 'cotizaciones.html', {'cotizaciones': cotizaciones})

def lista_detalles_cotizacion(request):
    detalles = Cotizacion_Detalle.objects.all()
    return render(request, 'cotizacion_detalle.html', {'detalles': detalles})

def lista_compras_carro(request):
    compras = Compra_Carro.objects.all()
    return render(request, 'compras_carro.html', {'compras': compras})

def lista_compras_repuesto(request):
    compras = Compra_Repuesto.objects.all()
    return render(request, 'compras_repuesto.html', {'compras': compras})

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores.html', {'proveedores': proveedores})

def bitacora_alertas(request):
    alertas = Bitacora_Alertas.objects.all()
    return render(request, 'bitacora_alertas.html', {'alertas': alertas})

def historial_cambio(request):
    cambios = Historial_Cambio.objects.all()
    return render(request, 'historial_cambio.html', {'cambios': cambios})

def cambios_salarios(request):
    cambios = Cambios_Salarios.objects.all()
    return render(request, 'cambios_salarios.html', {'cambios': cambios})