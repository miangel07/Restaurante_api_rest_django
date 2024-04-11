
from rest_framework import viewsets
from pedidos.models import Pedidos
from pedidos.api.Serializer import PedidosSerializer
class productosViewSet(viewsets.ModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer
