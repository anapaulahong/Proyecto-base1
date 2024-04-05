from django.urls import path
from . import views

urlpatterns = [
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('carros/', views.lista_carros, name='lista_carros'),
    path('repuestos/', views.lista_repuestos, name='lista_repuestos'),
    path('inventario/', views.lista_inventario, name='lista_inventario'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('ventas/', views.lista_ventas, name='lista_ventas'),
    path('detalles-venta/', views.detalles_venta, name='detalles_venta'),
    path('comisiones/', views.lista_comisiones, name='lista_comisiones'),
    path('departamentos/', views.lista_departamentos, name='lista_departamentos'),
    path('pagos/', views.lista_pagos, name='lista_pagos'),
    path('cotizaciones/', views.lista_cotizaciones, name='lista_cotizaciones'),
    path('cotizacion_detalles/', views.lista_detalles_cotizacion, name='lista_detalles_cotizacion'),
    path('compras_carro/', views.lista_compras_carro, name='lista_compras_carro'),
    path('compras_repuesto/', views.lista_compras_repuesto, name='lista_compras_repuesto'),
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('bitacora_alertas/', views.bitacora_alertas, name='bitacora_alertas'),
    path('historial_cambio/', views.historial_cambio, name='historial_cambio'),
    path('cambios_salarios/', views.cambios_salarios, name='cambios_salarios'),
]


