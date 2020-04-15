from django.shortcuts import render
from django.http import HttpResponse
from GestionPedidos.models import Clientes, Articulos, Pedidos
# Create your views here.
# GIT URL: https://github.com/Gambl3r08/TiendaOnline.git

def busqueda_procutos(request):
    return render(request, 'busqueda_productos.html')

def buscar(request):
    if request.GET["producto"]:
        # mensaje = "Artículo buscado: " + request.GET["producto"]
        producto_l = request.GET["producto"]
        articulos = Articulos.objects.filter(nombre__icontains=producto_l)
        return render(request, 'resultado_busqueda.html', {"articulos":articulos, "query":producto_l})

    else:
        mensaje = "No has introducido nada"

    return HttpResponse(mensaje)