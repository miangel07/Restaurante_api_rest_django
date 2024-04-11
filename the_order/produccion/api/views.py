from rest_framework import viewsets
from produccion.models import Factura
from produccion.api.Serializer import FacturaSerializer
from pedidos.models import Pedidos

class FacturaSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
