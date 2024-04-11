from django.urls import path,include
from productos.api.views import productosViewSet
from rest_framework import routers
router_productos = routers.DefaultRouter()
router_productos.register(prefix='productos',basename='productos',viewset=productosViewSet)