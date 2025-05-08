from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import (
    generar_reporte_inventario_excel,
    generar_reporte_inventario_pdf,
)
from django.shortcuts import render

class ReporteInventarioAPIView(APIView):
    def get(self, request):
        formato = request.query_params.get('formato')
        tipo = request.query_params.get('tipo_reporte')
        fecha_inicio = request.query_params.get('fecha_inicio')
        fecha_fin = request.query_params.get('fecha_fin')
        
        if not all([formato, tipo, fecha_inicio, fecha_fin]):
            return Response({"error": "Faltan parámetros requeridos."}, status=status.HTTP_400_BAD_REQUEST)
        
        if tipo == 'productos':
            if formato == 'excel':
                return generar_reporte_inventario_excel(fecha_inicio, fecha_fin)
            elif formato == 'pdf':
                return generar_reporte_inventario_pdf(fecha_inicio, fecha_fin)
            else:
                return Response({"error": "Formato no válido."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Tipo de reporte no válido."}, status=status.HTTP_400_BAD_REQUEST)
        

def frontend_reportes(request):
    return render(request, 'reportes/reportes.html')