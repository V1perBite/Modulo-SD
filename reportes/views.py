from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse
from .services import (
    generar_reporte_ventas_excel,
    generar_reporte_ventas_pdf,
    generar_reporte_inventario_excel,
    generar_reporte_inventario_pdf,
    generar_reporte_distribucion_excel,
    generar_reporte_distribucion_pdf
)

def vista_reportes(request):
    if request.method == 'POST':
        formato = request.POST.get('formato')
        tipo = request.POST.get('tipo_reporte')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        region = request.POST.get('region')
        producto = request.POST.get('producto')

        if tipo == 'ventas':
            if formato == 'excel':
                return generar_reporte_ventas_excel(fecha_inicio, fecha_fin, region, producto)
            elif formato == 'pdf':
                return generar_reporte_ventas_pdf(fecha_inicio, fecha_fin, region, producto)

        elif tipo == 'inventario':
            if formato == 'excel':
                return generar_reporte_inventario_excel(fecha_inicio, fecha_fin, region, producto)
            elif formato == 'pdf':
                return generar_reporte_inventario_pdf(fecha_inicio, fecha_fin, region, producto)

        elif tipo == 'distribucion':
            if formato == 'excel':
                return generar_reporte_distribucion_excel(fecha_inicio, fecha_fin, region, producto)
            elif formato == 'pdf':
                return generar_reporte_distribucion_pdf(fecha_inicio, fecha_fin, region, producto)

    return render(request, 'reportes/formulario.html')


    # Aqui estan la APIViews para manejar las solicitudes de generación de reportes en formato Excel o PDF.

class ReporteArchivoAPIView(APIView):
    def get(self, request):
        formato = request.query_params.get('formato')
        tipo = request.query_params.get('tipo_reporte')
        fecha_inicio = request.query_params.get('fecha_inicio')
        fecha_fin = request.query_params.get('fecha_fin')
        region = request.query_params.get('region')
        producto = request.query_params.get('producto')

        if not all([formato, tipo]):
            return Response({'error': 'Parámetros requeridos faltantes.'}, status=status.HTTP_400_BAD_REQUEST)

        if tipo == 'ventas':
            if formato == 'excel':
                return generar_reporte_ventas_excel(fecha_inicio, fecha_fin, region, producto)
            elif formato == 'pdf':
                return generar_reporte_ventas_pdf(fecha_inicio, fecha_fin, region, producto)

        elif tipo == 'inventario':
            if formato == 'excel':
                return generar_reporte_inventario_excel(fecha_inicio, fecha_fin, region, producto)
            elif formato == 'pdf':
                return generar_reporte_inventario_pdf(fecha_inicio, fecha_fin, region, producto)

        elif tipo == 'distribucion':
            if formato == 'excel':
                return generar_reporte_distribucion_excel(fecha_inicio, fecha_fin, region, producto)
            elif formato == 'pdf':
                return generar_reporte_distribucion_pdf(fecha_inicio, fecha_fin, region, producto)

        return Response({'error': 'Combinación tipo/formato no válida.'}, status=status.HTTP_400_BAD_REQUEST)