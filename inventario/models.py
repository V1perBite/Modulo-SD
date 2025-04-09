from django.db import models
from django.core.exceptions import ValidationError

# This is a Django model for a product in an inventory system.Models are used to define the structure of the database tables.
# Each model corresponds to a table in the database, and each attribute of the model corresponds to a column in the table.
# The model includes fields for the product's name, description, categories, supplier, image, purchase price, sale price, stock quantity, and creation date.
# The model also includes a method to validate that the sale price is not less than the purchase price and that the stock quantity is not negative.
class Producto(models.Model):
    nombre = models.CharField('Nombre del producto', max_length=100)
    descripcion = models.TextField('Descripción del producto')
    categorias = models.ManyToManyField('Categoria', related_name='productos', verbose_name='Categorías')
    proveedor = models.ForeignKey('Proveedor', verbose_name='Proveedor', on_delete=models.CASCADE, related_name='productos')
    imagen = models.ImageField('Imagen del producto', upload_to='productos/', null=True, blank=True)
    precio_compra = models.DecimalField('Precio de compra del producto', max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField('Precio de venta del producto', max_digits=10, decimal_places=2)
    stock = models.IntegerField('Cantidad de unidades', default=0)
    fecha_creacion = models.DateTimeField('Fecha de creación', auto_now_add=True)

    def __str__(self):
        return self.nombre

    def clean(self):
        if self.precio_venta < self.precio_compra:
            raise ValidationError('El precio de venta no puede ser menor que el precio de compra.')
        if self.stock < 0:
            raise ValidationError('El stock no puede ser negativo.')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        
        
class  Categoria(models.Model):
    pass

class Entry(models.Model):
    pass

class Proveedor(models.Model):
    pass


