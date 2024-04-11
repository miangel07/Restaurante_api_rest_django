from rest_framework.serializers import  ModelSerializer
from productos.models import Productos

class ProductosSerializer(ModelSerializer):
     class Meta:
         model = Productos
         fields = ['nombre','precio', 'stock']
