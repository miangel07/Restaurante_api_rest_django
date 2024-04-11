from django.urls import path,include
from produccion.api.views import FacturaSet
from rest_framework import routers
router_factura = routers.DefaultRouter()
router_factura.register(prefix='factura',basename='factura',viewset=FacturaSet)