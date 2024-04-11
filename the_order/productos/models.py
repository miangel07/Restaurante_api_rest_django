from django.db import models

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    precio =models.DecimalField(max_digits=10 , decimal_places=3)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre
