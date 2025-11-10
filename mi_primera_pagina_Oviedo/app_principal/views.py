from django.shortcuts import render
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'app_principal/lista_objetos.html', {'productos': productos})
