# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^json_get_precio/$',
        'servicios.views.json_get_precio',
        name='json_get_precio'),
    url(r'^json_get_precios_producto/$',
        'creditos.views.json_get_precios_producto',
        name='json_get_precios_producto'),
    url('^', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$','django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT,'show_indexes': True}),
    (r'^static/(?P<path>.*)$','django.views.static.serve',
         {'document_root': settings.STATIC_ROOT,'show_indexes': True}),
)
