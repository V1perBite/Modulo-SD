from django.urls import path
from .views import vista_reportes

urlpatterns = [
    path('nuevo_formulario/', vista_reportes, name='vista_reportes'),
]