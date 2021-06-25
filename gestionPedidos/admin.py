from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos


# migra los modelos a el panel de admon de Django
admin.site.register(Clientes)
admin.site.register(Articulos)
admin.site.register(Pedidos)
