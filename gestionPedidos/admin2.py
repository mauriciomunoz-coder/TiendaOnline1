from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos


#
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'email', 'tfno')  # muestra los datos de los registros
    search_fields = ( 'nombre', 'direccion', 'email', 'tfno')  # pone la barra de busqueda por nombre, direccion o telefono


admin.site.register(Clientes, ClientesAdmin)


class ArticulosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'seccion', 'precio')


admin.site.register(Articulos, ArticulosAdmin)


class PedidosAdmin(admin.ModelAdmin):
    list_display = ('numero', 'fecha', 'entregado')


admin.site.register(Pedidos, PedidosAdmin)
