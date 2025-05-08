from django.urls import path
from .views import vista_reportes, ReporteArchivoAPIView

urlpatterns = [
    path('nuevo_formulario/', vista_reportes, name='vista_reportes'),
    path('api/reportes/', ReporteArchivoAPIView.as_view(), name='api-reportes'),

]