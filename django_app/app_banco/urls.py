# app_banco/urls.py

from django.urls import path
from . import views

urlpatterns = [
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
]
