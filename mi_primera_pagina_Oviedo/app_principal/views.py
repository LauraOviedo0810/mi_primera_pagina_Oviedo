from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def lista_productos(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_productos")  # evita re-enviar formularios
    else:
        form = ProductoForm()

    productos = Producto.objects.all()

    return render(request, "app_principal/lista_objetos.html", {
        "form": form,
        "productos": productos
    })