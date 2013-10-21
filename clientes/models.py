# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.options import get_verbose_name


class TipoDocumento(models.Model) :
    """
    Tipo de documento de entedad
    """
    abreviatura = models.CharField(max_length=5)
    descripcion = models.CharField(max_length=50, verbose_name=u"descripción")

    def __unicode__(self):
        return u"%s" % self.abreviatura


class Entidad(models.Model):
    """
    tabla de entidades
    """
    codigo_entidad = models.CharField(max_length=8,
                                      verbose_name=u"código de entidad")
    tipo_documento = models.ForeignKey(TipoDocumento,
                                       verbose_name=u"tipo de documento")
    numero_documento = models.CharField(max_length=11, null=True, blank=True,
                                        verbose_name=u"número de documento")
    TIPO_PERSONA_CHOICES = (
        (u"N", u"Natural"),
        (u"J", u"Juridica"),
    )
    tipo_persona = models.CharField(max_length=1, choices=TIPO_PERSONA_CHOICES,
                                    verbose_name=u"tipo de persona")
    apellido_paterno = models.CharField(max_length=25, null=True, blank=True)
    apellido_materno = models.CharField(max_length=25, null=True, blank=True)
    nombres = models.CharField(max_length=50, null=True, blank=True)
    razon_social = models.CharField(max_length=100,
                                    verbose_name=u"razón social")
    fecha_nacimiento = models.DateField(null=True, blank=True,
                                        verbose_name=u"fecha de nacimiento")
    direccion = models.CharField(max_length=100, null=True, blank=True,
                                 verbose_name=u"dirección")
    direccion_extra = models.CharField(max_length=100, null=True, blank=True,
                                       verbose_name=u"dirección alternativa")
    telefono_fijo = models.CharField(max_length=12, null=True, blank=True,
                                     verbose_name=u"teléfono fijo")
    telefono_celular = models.CharField(max_length=12, null=True, blank=True,
                                        verbose_name=u"teléfono celular")
    email = models.EmailField(null=True, blank=True)

    def __unicode__(self):
        return u"%s" % self.razon_social

    # TODO: Con tipo de persona se activan lso nombres o la razón social,
    # en razón social se guarda todo concatenado
    def get_nombre_completo(self):
        return u"%s" % (self.nombres, self.apellido_paterno)

    class Meta:
        abstract = True
        verbose_name_plural = u"Entidades"


class Cliente(Entidad):
    """

    """
    class Meta:
        verbose_name_plural = u"Clientes"
    pass


class Proveedor(Entidad):
    """

    """
    class Meta:
        verbose_name = u"Proveedor"
        verbose_name_plural = u"Proveedores"
    pass


class Socio(Entidad):
    """

    """
    class Meta:
        verbose_name = u"Socio"
        verbose_name_plural = u"Socios"
    pass


class Empleado(Entidad):
    """

    """
    class Meta:
        verbose_name = u"Empleado"
        verbose_name_plural = u"Empleados"
    pass