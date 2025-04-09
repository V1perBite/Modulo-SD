from django.shortcuts import render
from .forms import EntryForm, ProductoForm


def index(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'inventario/index.html',{
                "form": ProductoForm(),
                "Message": "Entrada registrada correctamente"
            } )
            
        else:
            form = EntryForm()
            return render(request, 'inventario/index.html',{'form': ProductoForm()})
