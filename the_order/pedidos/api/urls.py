from django.urls import path,include
from pedidos.api.views import productosViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(prefix='pedido',basename='pedido',viewset=productosViewSet)
