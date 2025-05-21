from django.urls import path
from .views import listar_productos, historial_entradas


urlpatterns = [
    path('productos/', listar_productos, name='listar_productos'),
    path('entradas/', historial_entradas, name='historial_entradas'),
]
