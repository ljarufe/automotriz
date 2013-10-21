# -*- coding: utf-8 -*-

from django.db import models
from clientes.models import Cliente, Proveedor


class Credito(models.Model):
    """

    """
    TIPO_CREDITO_CHOICES = (
        (u"C", u"Compra"),
        (u"V", u"Venta"),
    )
    tipo_credito = models.CharField(max_length=1, choices=TIPO_CREDITO_CHOICES,
                                    verbose_name=u"tipo de crédito")
    cliente = models.ForeignKey(Cliente, null=True, blank=True)
    proveedor = models.ForeignKey(Proveedor, null=True, blank=True)
    capital_pactado = models.FloatField()
    saldo_capital = models.FloatField()
    numero_cuotas = models.IntegerField(verbose_name=u"número de cuotas")
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    estado_credito = models.BooleanField()

    def __unicode__(self):
        return u"%s - %s - %s" % (self.tipo_credito, self.cliente,
                                  self.proveedor)

    def get_capital_pagado(self):
        return self.capital_pactado - self.saldo_capital

    class Meta:
        verbose_name = u"crédito"
        verbose_name_plural = u"créditos"


class PlanPago(models.Model):
    """

    """
    credito = models.ForeignKey(Credito, verbose_name=u"crédito")
    numero_cuota = models.IntegerField(verbose_name=u"número de cuota")
    estado_cuota = models.BooleanField(verbose_name=u"estado de cuota")
    capital_pactado = models.FloatField()
    capital_pagado = models.FloatField()
    fecha_vencimiento = models.DateField(verbose_name=u"fecha de vencimiento")

    def __unicode__(self):
        return u"%s - %s" % (self.fecha_vencimiento, self.numero_cuota)

    class Meta:
        verbose_name = u"plan de pago"
        verbose_name_plural = u"plan de pagos"