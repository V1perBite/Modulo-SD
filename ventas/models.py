from django.db import models
from inventario.models import Producto

# Create your models here.
class venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_venta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venta de {self.cantidad} unidades de {self.producto.nombre} el {self.fecha_venta}"