# Generated by Django 4.2.20 on 2025-04-09 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de la categoría')),
                ('descripcion', models.TextField(blank=True, verbose_name='Descripción de la categoría')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del proveedor')),
                ('direccion', models.CharField(max_length=200, verbose_name='Dirección del proveedor')),
                ('telefono', models.CharField(max_length=15, verbose_name='Teléfono del proveedor')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email del proveedor')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del producto')),
                ('descripcion', models.TextField(verbose_name='Descripción del producto')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos/', verbose_name='Imagen del producto')),
                ('precio_compra', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio de compra del producto')),
                ('precio_venta', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio de venta del producto')),
                ('stock', models.IntegerField(default=0, verbose_name='Cantidad de unidades')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('categorias', models.ManyToManyField(related_name='productos', to='inventario.categoria', verbose_name='Categorías')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='inventario.proveedor', verbose_name='Proveedor')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad de unidades')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de entrada')),
                ('observaciones', models.TextField(blank=True, verbose_name='Observaciones')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entradas', to='inventario.producto')),
            ],
        ),
    ]
