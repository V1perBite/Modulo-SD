from django import forms
from .models import Producto, Categoria, Proveedor, Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['producto', 'cantidad', 'observaciones']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'producto': 'Producto',
            'cantidad': 'Cantidad',
            'observaciones': 'Observaciones',
        }
        help_texts = {
            'producto': 'Seleccione el producto al que desea añadir stock.',
            'cantidad': 'Ingrese la cantidad de unidades a añadir.',
            'observaciones': 'Ingrese cualquier observación adicional.',
        }
        error_messages = {
            'producto': {
                'required': 'Este campo es obligatorio.',
            },
            'cantidad': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese un número válido.',
            },
            'observaciones': {
                'max_length': 'Este campo no puede tener más de 200 caracteres.',
            },
        }
        
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'categorias', 'proveedor', 'imagen', 'precio_compra', 'precio_venta', 'stock']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del producto'}),
            'categorias': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Categorías'}),
            'proveedor': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Proveedor'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Imagen del producto'}),
            'precio_compra': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio de compra'}),
            'precio_venta': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio de venta'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad de unidades'}),
        }
        labels = {
            'nombre': 'Nombre del producto',
            'descripcion': 'Descripción del producto',
            'categorias': 'Categorías',
            'proveedor': 'Proveedor',
            'imagen': 'Imagen del producto',
            'precio_compra': 'Precio de compra',
            'precio_venta': 'Precio de venta',
            'stock': 'Cantidad de unidades',
        }
       
        error_messages = {
            'nombre': {
                'required': 'Este campo es obligatorio.',
                'max_length': 'Este campo no puede tener más de 100 caracteres.',
            },
            'descripcion': {
                'required': 'Este campo es obligatorio.',
            },
            'categorias': {
                'required': 'Este campo es obligatorio.',
            },
            'proveedor': {
                'required': 'Este campo es obligatorio.',
            },
            'precio_compra': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese un número válido.',
            },
            'precio_venta': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese un número válido.',
            },
            'stock': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese un número válido.',
            },
        }
        
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'direccion', 'telefono', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del proveedor'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección del proveedor'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono del proveedor'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email del proveedor'}),
        }
        labels = {
            'nombre': 'Nombre del proveedor',
            'direccion': 'Dirección del proveedor',
            'telefono': 'Teléfono del proveedor',
            'email': 'Email del proveedor',
        }
        
        error_messages = {
            'nombre': {
                'required': 'Este campo es obligatorio.',
                'max_length': 'Este campo no puede tener más de 100 caracteres.',
            },
            'direccion': {
                'required': 'Este campo es obligatorio.',
            },
            'telefono': {
                'required': 'Este campo es obligatorio.',
                'invalid': 'Ingrese un número válido.',
            },
            'email': {
                'invalid': 'Ingrese un email válido.',
            },
        }
        
class CategoriaForm(forms.ModelForm):
    class Meta: 
        model = Categoria
        fields = ['name', 'descripcion']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la categoría'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción de la categoría'}),
        }
        labels = {
            'name': 'Nombre de la categoría',
            'descripcion': 'Descripción de la categoría',
        }
        
        error_messages = {
            'name': {
                'required': 'Este campo es obligatorio.',
                'max_length': 'Este campo no puede tener más de 100 caracteres.',
            },
            'descripcion': {
                'required': 'Este campo es obligatorio.',
            },
        }