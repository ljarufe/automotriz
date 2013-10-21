# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models
from clientes.models import Cliente, Empleado


class TipoServicio(models.Model):
    """

    """
    descripcion = models.CharField(max_length=60, verbose_name=u"descripción")
    precio_base = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return u"%s" % self.descripcion


class Servicio(models.Model):
    """

    """
    tipo_servicio = models.ForeignKey(TipoServicio,
                                      verbose_name=u"tipo de servicio")
    cliente = models.ForeignKey(Cliente)
    precio = models.FloatField()
    empleado = models.ForeignKey(Empleado, null=True, blank=True)
    fecha = models.DateField(default=datetime.now)

    def __unicode__(self):
        return u"%s - %s - %s" % (self.cliente, self.tipo_servicio, self.fecha)
