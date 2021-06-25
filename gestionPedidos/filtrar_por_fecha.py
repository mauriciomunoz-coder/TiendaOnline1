from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos


# Register your models here.
class PedidosAdmin(admin.ModelAdmin):
    list_display = ('numero', 'fecha', 'entregado') # muestra estos campos en el panel de admon
    list_filter = ('fecha',)  # pone una tabla para filtrar por fecha
    date_hierarchy = 'fecha'  # pone de forma horizontal una barra para filtrar por mes


admin.site.register(Pedidos, PedidosAdmin)
