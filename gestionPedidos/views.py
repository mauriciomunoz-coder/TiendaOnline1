from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def busqueda_productos(request):
    return render(request, "busqueda_productos.html")


def buscar(request):
    #mensaje = "articulo buscado: %r" % request.GET["prd"]
    mensaje = f'articulo buscado: {request.GET["prd"]}'
    return HttpResponse(mensaje)
