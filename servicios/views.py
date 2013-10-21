# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from common.utils import json_response
from servicios.models import TipoServicio


@login_required
def json_get_precio(request):
    """

    """
    if "id_tipo_servicio" in request.GET:
        tipo_servicio = get_object_or_404(TipoServicio,
                                          id=request.GET["id_tipo_servicio"])

        return json_response({"precio": tipo_servicio.precio_base})
    else:
        return json_response({})