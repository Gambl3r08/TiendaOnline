from django.contrib import admin
from GestionPedidos.models import Clientes, Articulos, Pedidos
# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion',  'email','telefono')
    search_fields = ('nombre', 'direccion', 'email','telefono')

class ArticulosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'seccion', 'precio')
    search_fields = ('nombre', 'seccion', 'precio')

class PedidosAdmin(admin.ModelAdmin):
    list_display = ('numero', 'fecha', 'entregado')
    list_display = ('numero', 'fecha', 'entregado')
    date_hierarchy = ('fecha')

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos)