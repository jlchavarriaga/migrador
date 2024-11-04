# app_banco/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('instituciones/', views.institucion_list, name='institucion_list'),
    path('instituciones/nueva/', views.institucion_create, name='institucion_create'),
    path('instituciones/<int:pk>/editar/', views.institucion_update, name='institucion_update'),
    path('instituciones/<int:pk>/eliminar/', views.institucion_delete, name='institucion_delete'),

    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/<int:pk>/', views.cliente_detail, name='cliente_detail'),
    path('clientes/new/', views.cliente_create, name='cliente_create'),
    path('clientes/<int:pk>/edit/', views.cliente_update, name='cliente_update'),
    path('clientes/<int:pk>/delete/', views.cliente_delete, name='cliente_delete'),

    path('cuentas/', views.cuenta_list, name='cuenta_list'),
    path('cuentas/<int:pk>/', views.cuenta_detail, name='cuenta_detail'),
    path('cuentas/new/', views.cuenta_create, name='cuenta_create'),
    path('cuentas/<int:pk>/edit/', views.cuenta_update, name='cuenta_update'),
    path('cuentas/<int:pk>/delete/', views.cuenta_delete, name='cuenta_delete'),

    path('cargar_transacciones/', views.cargar_transacciones, name='cargar_transacciones'),
    path('descargar_transacciones/', views.descargar_transacciones, name='descargar_transacciones'),

    path('cuenta/<int:cuenta_id>/transacciones/', views.transacciones_por_cuenta, name='transacciones_por_cuenta'),

]
