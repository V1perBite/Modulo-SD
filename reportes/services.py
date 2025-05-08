import openpyxl
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from inventario.models import Producto



def generar_reporte_inventario_excel(fecha_inicio, fecha_fin):
    # Crear un libro de trabajo y una hoja
    libro = openpyxl.Workbook()
    hoja = libro.active
    hoja.title = 'Productos'

    # Definir los encabezados
    encabezados = ['ID', 'Nombre',  'Precio de compra', 'Precio de venta', 'Stock']
    hoja.append(encabezados)

    # Obtener todos los productos
    productos = Producto.objects.all()

    # Agregar los datos de los productos a la hoja
    for producto in productos:
        fila = [
            producto.id,
            producto.nombre,
            producto.precio_compra,
            producto.precio_venta,
            producto.stock,
        ]
        hoja.append(fila)

    # Guardar el archivo Excel
    nombre_archivo = 'productos.xlsx'
    libro.save(nombre_archivo)

    # Devolver el archivo como respuesta HTTP
    with open(nombre_archivo, 'rb') as archivo:
        response = HttpResponse(archivo.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename={nombre_archivo}'
        return response
    
def generar_reporte_inventario_pdf(fecha_inicio, fecha_fin):
    # Crear un objeto HttpResponse con el tipo de contenido adecuado
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="productos.pdf"'

    # Crear un objeto Canvas para generar el PDF
    pdf = canvas.Canvas(response)

    # Definir la posición inicial
    x = 50
    y = 800

    # Escribir el título
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(x, y, "Reporte de Productos")
    y -= 30

    # Definir los encabezados
    pdf.setFont("Helvetica-Bold", 12)
    encabezados = ['ID', 'Nombre', 'Precio de compra', 'Precio de venta', 'Stock']
    for i, encabezado in enumerate(encabezados):
        pdf.drawString(x + i * 100, y, encabezado)
    
    y -= 20

    # Obtener todos los productos
    productos = Producto.objects.all()

    # Agregar los datos de los productos al PDF
    pdf.setFont("Helvetica", 12)
    for producto in productos:
        fila = [
            str(producto.id),
            producto.nombre,
            str(producto.precio_compra),
            str(producto.precio_venta),
            str(producto.stock),
        ]
        for i, dato in enumerate(fila):
            pdf.drawString(x + i * 100, y, dato)
        y -= 20

    # Finalizar el PDF
    pdf.showPage()
    pdf.save()

    return response


def generar_reporte_ventas_pdf(fecha_inicio, fecha_fin):
    # Implementar la lógica para generar el reporte de ventas en PDF
    pass
def generar_reporte_ventas_excel(fecha_inicio, fecha_fin):
    # Implementar la lógica para generar el reporte de ventas en Excel
    pass

def generar_reporte_distribucion_pdf(fecha_inicio, fecha_fin):
    # Implementar la lógica para generar el reporte de distribución en PDF
    pass
def generar_reporte_distribucion_excel(fecha_inicio, fecha_fin):
    # Implementar la lógica para generar el reporte de distribución en Excel
    pass