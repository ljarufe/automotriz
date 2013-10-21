# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from almacenes.models import PrecioProducto
from common.utils import json_response


@login_required
def json_get_precios_producto(request):
    """

    """
    if "id_producto" in request.GET:
        precios = [{"id": precio.id, "nombre": precio.__unicode__()}
                   for precio in
                   PrecioProducto.objects.filter(
                       producto=request.GET["id_producto"])]

        return json_response(precios)
    else:
        return json_response({})