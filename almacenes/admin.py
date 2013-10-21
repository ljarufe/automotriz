# -*- coding: utf-8 -*-

from django.contrib import admin
from almacenes.models import Marca, Unidad, Producto, PrecioProducto, Sucursal,\
    Almacen, ProductoAlmacen


class AlmacenAdmin(admin.ModelAdmin):
    list_display = ("descripcion", "sucursal",)


class MarcaAdmin(admin.ModelAdmin):
    list_display = ("descripcion", "abreviatura",)


class SucursalAdmin(admin.ModelAdmin):
    list_display = ("descripcion", "direccion", "telefono",)


class UnidadAdmin(admin.ModelAdmin):
    list_display = ("descripcion", "abreviatura",)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ("codigo", "descripcion", "abreviatura", "medida", "aro",
                    "pr",)


admin.site.register(Marca, MarcaAdmin)
admin.site.register(Unidad, UnidadAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(PrecioProducto)
admin.site.register(Sucursal, SucursalAdmin)
admin.site.register(Almacen, AlmacenAdmin)
admin.site.register(ProductoAlmacen)