from django.urls import path
from .views import index
#from .views import index, productos, proveedores, entradas, categorias


urlpatterns = [
    path('', index, name='index'),
    # path('productos/', productos, name='productos'),
    # path('proveedores/', proveedores, name='proveedores'),
    # path('entradas/', entradas, name='entradas'),
    # path('categorias/', categorias, name='categorias')
]
