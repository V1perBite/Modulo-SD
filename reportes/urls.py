from django.urls import path
from .views import  ReporteInventarioAPIView, frontend_reportes

urlpatterns = [
    path('api/reportes/', ReporteInventarioAPIView.as_view(), name='api-reportes'),
    path('reportes/', frontend_reportes, name='frontend-reportes'),

]
