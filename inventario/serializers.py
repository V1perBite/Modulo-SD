from rest_framework import serializers
from .models import Producto, Entry

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'  # O puedes especificar los campos que quieres incluir

class EntrySerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)  # Para mostrar los datos del producto relacionado

    class Meta:
        model = Entry
        fields = '__all__'