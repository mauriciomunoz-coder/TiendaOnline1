from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos


# Create your views here.


def busqueda_productos(request):
    return render(request, "busqueda_productos.html")


def buscar(request):
    # mensaje = "articulo buscado: %r" % request.GET["prd"]
    if request.GET['prd'] != "":

        # mensaje = f'articulo buscado: {request.GET["prd"]}'
        producto = request.GET['prd']

        articulos = Articulos.objects.filter(nombre__icontains=producto)

        return render(request, "resultados_busqueda.html", {"articulos": articulos, "consulta": producto})
    else:
        mensaje = 'debes introducir algun valor'
    return HttpResponse(mensaje)
