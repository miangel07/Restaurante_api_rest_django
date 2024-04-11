from rest_framework.serializers import ModelSerializer
from produccion.models import Factura
from pedidos.api.Serializer import PedidosSerializer
from productos.api.Serializer import ProductosSerializer

class FacturaSerializer(ModelSerializer):
    pedido = PedidosSerializer()
    productos = ProductosSerializer()

    class Meta:
        model = Factura
        fields = ['pedido', 'productos', ]
