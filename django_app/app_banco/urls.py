# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InstitucionViewSet, ClienteViewSet, CuentaViewSet, TransaccionViewSet

router = DefaultRouter()
router.register(r'instituciones', InstitucionViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'cuentas', CuentaViewSet)
router.register(r'transacciones', TransaccionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
