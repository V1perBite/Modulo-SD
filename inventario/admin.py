from django.contrib import admin
from .models import Producto, Categoria, Proveedor, Entry


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_compra', 'precio_venta', 'stock', 'fecha_creacion')
    list_filter = ('proveedor', 'categorias')
    search_fields = ('nombre',)
    
    
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email')
    search_fields = ('nombre',)
    
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'fecha', 'observaciones')
    list_filter = ('producto', 'fecha')