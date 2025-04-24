from django.shortcuts import render
from .models import Producto, Entry
from django.core.paginator import Paginator

def listar_productos(request):
    productos_list = Producto.objects.order_by('id')
    paginator = Paginator(productos_list, 10)  # 10 productos por página
    page_number = request.GET.get('page')
    productos = paginator.get_page(page_number)
    return render(request, 'inventario/listar_productos.html', {'productos': productos})

def historial_entradas(request):
    entradas = Entry.objects.select_related('producto').order_by('-id')
    return render(request, 'inventario/historial_entradas.html', {'entradas': entradas})


def reporte_pdf(request):
    pass

def reporte_excel(request):
    pass
