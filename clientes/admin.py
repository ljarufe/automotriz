# -*- coding: utf-8 -*-

from django.contrib import admin
from clientes.models import TipoDocumento, Cliente, Proveedor, Socio, Empleado


class EntidadAdmin(admin.ModelAdmin):
    list_display = ("razon_social", "tipo_documento", "numero_documento",
                    "telefono_fijo", "telefono_celular",)


admin.site.register(TipoDocumento)
admin.site.register(Cliente, EntidadAdmin)
admin.site.register(Proveedor, EntidadAdmin)
admin.site.register(Socio, EntidadAdmin)
admin.site.register(Empleado, EntidadAdmin)