from django.shortcuts import render, redirect
from .models import Producto

def lista_productos(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")
        descripcion = request.POST.get("descripcion")

        Producto.objects.create(
            nombre=nombre,
            precio=precio,
            descripcion=descripcion
        )
        return redirect('lista_productos')

    productos = Producto.objects.all()
    return render(request, 'app_principal/lista_objetos.html', {'productos': productos})