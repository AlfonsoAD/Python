from django.contrib import admin
from .models import Categoria, Producto


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


class ProductoAdmin(admin.ModelAdmin):
    exclude = ('create_date',)
    list_display = ('id', 'nombre', 'stock', 'create_date')


# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
