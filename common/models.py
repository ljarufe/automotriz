# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models


class Constantes(models.Model):
    """

    """
    descripcion = models.CharField(max_length=100, verbose_name=u"descripción")
    valor = models.CharField(max_length=50)

    def __unicode__(self):
        return u"%s" % self.descripcion

    class Meta:
        verbose_name_plural = u"Constantes"


class CambioMoneda(models.Model):
    """

    """
    fecha = models.DateField(default=datetime.now)
    cambio = models.FloatField()

    def __unicode__(self):
        return u"%s: %s" % (self.fecha, self.cambio)

    class Meta:
        verbose_name = u"Cambio de moneda"
        verbose_name_plural = u"Cambios de moneda"


class TipoMoneda(models.Model):
    """

    """
    descripcion = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=5)

    def __unicode__(self):
        return u"%s" % self.descripcion