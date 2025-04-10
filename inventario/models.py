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
    name = models.CharField('Nombre de la categoría', max_length=100)
    descripcion = models.TextField('Descripción de la categoría', blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

class Entry(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='entradas')
    cantidad = models.IntegerField('Cantidad de unidades')
    fecha = models.DateTimeField('Fecha de entrada', auto_now_add=True)
    observaciones = models.TextField('Observaciones', blank=True)
    
    def save(self, *args, **kwargs):
        self.producto.stock += self.cantidad
        self.producto.save()
        super().save(*args, **kwargs)
    def __str__(self):
        return f'Entrada de {self.cantidad} unidades de {self.producto.nombre}'

class Proveedor(models.Model):
    nombre = models.CharField('Nombre del proveedor', max_length=100)
    direccion = models.CharField('Dirección del proveedor', max_length=200)
    telefono = models.CharField('Teléfono del proveedor', max_length=15)
    email = models.EmailField('Email del proveedor', blank=True)
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'


