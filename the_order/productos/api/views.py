from rest_framework import viewsets
from productos.models import Productos
from productos.api.Serializer import ProductosSerializer
class productosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

