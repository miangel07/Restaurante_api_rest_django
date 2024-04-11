from django.db import models
from django.db.models import SET_NULL
from pedidos.models import Pedidos
from productos.models import Productos

class Factura(models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=SET_NULL, null=True)
    productos = models.ForeignKey(Productos, on_delete=SET_NULL, null=True)
    
