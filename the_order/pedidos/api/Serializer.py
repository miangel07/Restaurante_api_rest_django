from rest_framework.serializers import  ModelSerializer
from pedidos.models import Pedidos

class PedidosSerializer(ModelSerializer):
     class Meta:
         model = Pedidos
         fields = ['cliente','para_llevar', 'observaciones','estado','cantidad','productos']