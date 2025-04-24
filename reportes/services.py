import openpyxl
from reportlab.pdfgen import canvas
from django.http import HttpResponse
import io

# ---- VENTAS ----

def generar_reporte_ventas_excel(fecha_inicio, fecha_fin, region, producto):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Reporte de Ventas"
    ws.append(["Fecha", "Producto", "Región", "Cantidad", "Total"])
    ws.append(["2024-01-10", "MacBook", "Norte", 5, 10000])
    ws.append(["2024-01-15", "iPhone", "Sur", 2, 3000])
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=ventas.xlsx'
    wb.save(response)
    return response

def generar_reporte_ventas_pdf(fecha_inicio, fecha_fin, region, producto):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 800, "Reporte de Ventas")
    p.drawString(100, 780, f"Producto: {producto}, Región: {region}")
    p.drawString(100, 760, "Ejemplo de línea de ventas.")
    p.showPage()
    p.save()
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')

# ---- INVENTARIO ----

def generar_reporte_inventario_excel(fecha_inicio, fecha_fin, region, producto):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Reporte de Inventario"
    ws.append(["Producto", "Stock Actual", "Ubicación"])
    ws.append(["MacBook", 10, "Almacén Central"])
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=inventario.xlsx'
    wb.save(response)
    return response

def generar_reporte_inventario_pdf(fecha_inicio, fecha_fin, region, producto):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 800, "Reporte de Inventario")
    p.drawString(100, 780, f"Producto: {producto}, Región: {region}")
    p.drawString(100, 760, "Stock actual simulado.")
    p.showPage()
    p.save()
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')

# ---- DISTRIBUCIÓN ----

def generar_reporte_distribucion_excel(fecha_inicio, fecha_fin, region, producto):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Reporte de Distribución"
    ws.append(["Fecha", "Producto", "Destino", "Cantidad"])
    ws.append(["2024-01-12", "iPad", "Sucursal Norte", 4])
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=distribucion.xlsx'
    wb.save(response)
    return response

def generar_reporte_distribucion_pdf(fecha_inicio, fecha_fin, region, producto):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 800, "Reporte de Distribución")
    p.drawString(100, 780, f"Producto: {producto}, Región: {region}")
    p.drawString(100, 760, "Ejemplo de distribución registrada.")
    p.showPage()
    p.save()
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')
