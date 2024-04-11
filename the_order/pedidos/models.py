from django.db import models
from productos.models import Productos
from django.db.models import SET_NULL
class Pedidos(models.Model):
    cliente = models.CharField(max_length=100)
    para_llevar = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, default='pendiente') 
    cantidad = models.CharField(max_length=20, default=1)
    productos = models.ForeignKey(Productos,  on_delete= SET_NULL,null= True)
    def __str__(self):
        return self.cliente