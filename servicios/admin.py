# -*- coding: utf-8 -*-

from django.contrib import admin
from servicios.models import TipoServicio, Servicio

admin.site.register(Servicio)
admin.site.register(TipoServicio)