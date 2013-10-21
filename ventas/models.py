# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models
from clientes.models import Cliente, Proveedor
from common.models import Constantes
from creditos.models import Credito
from almacenes.models import ProductoAlmacen, PrecioProducto


class CabeceraDocumento(models.Model):
    """

    """
    serie = models.CharField(max_length=5)
    numero = models.CharField(max_length=12)
    TIPO_DOCUMENTO_CHOICES = (
        (u"C", u"Compra"),
        (u"V", u"Venta"),
    )
    tipo_documento = models.CharField(max_length=1,
                                      choices=TIPO_DOCUMENTO_CHOICES,
                                      verbose_name=u"tipo de documento")
    cliente = models.ForeignKey(Cliente)
    proveedor = models.ForeignKey(Proveedor)
    fecha_valor = models.DateField(default=datetime.now,
                                   verbose_name=u"fecha de valor")
    fecha_proceso = models.DateField(default=datetime.now,
                                     null=True, blank=True,
                                     verbose_name=u"fecha de proceso")
    total = models.FloatField(default=0)
    TIPO_PAGO_CHOICES = (
        (u"Cr", u"Crédito"),
        (u"Co", u"Contado")
    )
    tipo_pago = models.CharField(max_length=2, default=u"Co",
                                 choices=TIPO_PAGO_CHOICES,
                                 verbose_name=u"Tipo de pago")
    credito = models.ForeignKey(Credito, null=True, blank=True,
                                verbose_name=u"crédito")
    observaciones = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return u"%s - %s" % (self.serie, self.numero)

    def get_subtotal(self):
        # TODO: buscar funcion de quitar espacios y de pasaranminusculas o mayusculaso minusculas
        try:
            igv = float(Constantes.objects.get(descripcion__like="igv"))
        except Constantes.DoesNotExist:
            igv = 18

        return self.total * igv / 100

    class Meta:
        verbose_name = u"Documento"
        verbose_name_plural = u"Documentos"


class DetalleDocumento(models.Model):
    """

    """
    cabecera = models.ForeignKey(CabeceraDocumento)
    cantidad = models.FloatField()
    producto_almacen = models.ForeignKey(ProductoAlmacen,
                                         verbose_name=u"producto")
    precio_producto = models.ForeignKey(PrecioProducto, verbose_name=u"precio",
                                        null=True, blank=True)
    precio = models.FloatField(default=0)

    def __unicode__(self):
        return u"%s, %s - %s" % (self.cabecera, self.producto_almacen,
                                 self.cantidad)