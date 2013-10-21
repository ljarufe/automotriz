# -*- coding: utf-8 -*-

from django.contrib import admin
from creditos.models import Credito, PlanPago


class PlanPagoInLine(admin.TabularInline):
    model = PlanPago
    extra = 0


class CreditoAdmin(admin.ModelAdmin):
    readonly_fields = ("estado_credito",)
    inlines = [PlanPagoInLine]


admin.site.register(Credito, CreditoAdmin)