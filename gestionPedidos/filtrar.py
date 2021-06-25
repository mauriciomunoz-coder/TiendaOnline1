from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

admin.site.register(Clientes)
admin.site.register(Articulos)
admin.site.register(Pedidos)


class ArticulosAdmin(admin.ModelAdmin):
    list_filter = ('seccion','nombre')  # agrega dos tablas en el panel de admon, una para filtrar por seccion y otra para filtrar por nombre


admin.site.register(Articulos, ArticulosAdmin)
