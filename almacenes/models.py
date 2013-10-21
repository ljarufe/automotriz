# -*- coding: utf-8 -*-

from django.db import models
from common.models import TipoMoneda


class Marca(models.Model):
    """

    """
    descripcion = models.CharField(max_length=100, verbose_name=u"descripción")
    abreviatura = models.CharField(max_length=5)

    def __unicode__(self):
        return u"%s" % self.descripcion


class Unidad(models.Model):
    """

    """
    descripcion = models.CharField(max_length=20, verbose_name=u"descripción")
    abreviatura = models.CharField(max_length=5)

    def __unicode__(self):
        return u"%s" % self.abreviatura

    class Meta:
        verbose_name_plural = u"Unidades"


class Producto(models.Model):
    """

    """
    codigo = models.CharField(max_length=20, verbose_name=u"código")
    descripcion = models.CharField(max_length=100, verbose_name=u"descripción")
    abreviatura = models.CharField(max_length=5)
    unidad = models.ForeignKey(Unidad, null=True, blank=True)
    medida = models.CharField(max_length=10, null=True, blank=True)
    aro = models.CharField(max_length=5, null=True, blank=True)
    pr = models.CharField(max_length=10, null=True, blank=True,
                          verbose_name=u"PR")
    uso = models.CharField(max_length=10, null=True, blank=True)

    def __unicode__(self):
        return u"%s" % self.descripcion


class PrecioProducto(models.Model):
    """

    """
    descripcion = models.CharField(max_length=20, verbose_name=u"descripción")
    #TODO: revisar como truncar a dos decimales al guardar
    tipo_moneda = models.ForeignKey(TipoMoneda, verbose_name=u"Tipo de moneda")
    precio = models.FloatField()
    producto = models.ForeignKey(Producto)
    TIPO_PRECIO_CHOICES = (
        (u"C", u"Compra"),
        (u"V", u"Venta"),
    )
    tipo_precio = models.CharField(max_length=1, choices=TIPO_PRECIO_CHOICES,
                                   verbose_name=u"tipo de precio")

    def __unicode__(self):
        return u"%s - %s" % (self.descripcion, self.precio)

    class Meta:
        verbose_name = u"Precio por producto"
        verbose_name_plural = u"Precios por producto"


class Sucursal(models.Model):
    """

    """
    descripcion = models.CharField(max_length=100, verbose_name=u"descripción")
    direccion = models.CharField(max_length=150, verbose_name=u"dirección")
    telefono = models.CharField(max_length=30, verbose_name=u"teléfono",
                                null=True, blank=True)

    def __unicode__(self):
        return u"%s" % self.descripcion

    class Meta:
        verbose_name_plural = u"Sucursales"


class Almacen(models.Model):
    """

    """
    descripcion = models.CharField(max_length=100, verbose_name=u"descripción")
    sucursal = models.ForeignKey(Sucursal)
    productos = models.ManyToManyField(Producto, through='ProductoAlmacen')

    def __unicode__(self):
        return u"%s" % self.descripcion

    class Meta:
        verbose_name = u"Almacén"
        verbose_name_plural = u"Almacenes"


class ProductoAlmacen(models.Model):
    """

    """
    producto = models.ForeignKey(Producto)
    almacen = models.ForeignKey(Almacen, verbose_name=u"almacén")
    unidades = models.FloatField()
    fecha_ultimo_movimiento = models.DateField(
        null=True, blank=True, verbose_name=u"fecha de último movimiento")

    def __unicode__(self):
        return u"%s - %s" % (self.producto, self.almacen)

    class Meta:
        verbose_name = u"Producto por almacén"
        verbose_name_plural = u"Productos por almacén"