# -*- coding: utf-8 -*-

from django.contrib import admin
from ventas.models import CabeceraDocumento, DetalleDocumento


class DetalleInLine(admin.TabularInline):
    model = DetalleDocumento


class CabeceraAdmin(admin.ModelAdmin):
    inlines = [DetalleInLine]


admin.site.register(CabeceraDocumento, CabeceraAdmin)