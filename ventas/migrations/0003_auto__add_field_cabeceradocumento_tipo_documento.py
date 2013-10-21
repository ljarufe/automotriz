# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CabeceraDocumento.tipo_documento'
        db.add_column(u'ventas_cabeceradocumento', 'tipo_documento',
                      self.gf('django.db.models.fields.CharField')(default='C', max_length=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CabeceraDocumento.tipo_documento'
        db.delete_column(u'ventas_cabeceradocumento', 'tipo_documento')


    models = {
        u'almacenes.almacen': {
            'Meta': {'object_name': 'Almacen'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['almacenes.Producto']", 'through': u"orm['almacenes.ProductoAlmacen']", 'symmetrical': 'False'}),
            'sucursal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacenes.Sucursal']"})
        },
        u'almacenes.precioproducto': {
            'Meta': {'object_name': 'PrecioProducto'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio': ('django.db.models.fields.FloatField', [], {}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacenes.Producto']"}),
            'tipo_moneda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['common.TipoMoneda']"}),
            'tipo_precio': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'almacenes.producto': {
            'Meta': {'object_name': 'Producto'},
            'abreviatura': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'aro': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medida': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'pr': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'unidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacenes.Unidad']", 'null': 'True', 'blank': 'True'}),
            'uso': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'almacenes.productoalmacen': {
            'Meta': {'object_name': 'ProductoAlmacen'},
            'almacen': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacenes.Almacen']"}),
            'fecha_ultimo_movimiento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacenes.Producto']"}),
            'unidades': ('django.db.models.fields.FloatField', [], {})
        },
        u'almacenes.sucursal': {
            'Meta': {'object_name': 'Sucursal'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        u'almacenes.unidad': {
            'Meta': {'object_name': 'Unidad'},
            'abreviatura': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'apellido_materno': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'apellido_paterno': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'codigo_entidad': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'direccion_extra': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'numero_documento': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'razon_social': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telefono_celular': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'telefono_fijo': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'tipo_documento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.TipoDocumento']"}),
            'tipo_persona': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'clientes.proveedor': {
            'Meta': {'object_name': 'Proveedor'},
            'apellido_materno': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'apellido_paterno': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'codigo_entidad': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'direccion_extra': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'numero_documento': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'razon_social': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telefono_celular': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'telefono_fijo': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'tipo_documento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.TipoDocumento']"}),
            'tipo_persona': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'clientes.tipodocumento': {
            'Meta': {'object_name': 'TipoDocumento'},
            'abreviatura': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'common.tipomoneda': {
            'Meta': {'object_name': 'TipoMoneda'},
            'abreviatura': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'creditos.credito': {
            'Meta': {'object_name': 'Credito'},
            'capital_pactado': ('django.db.models.fields.FloatField', [], {}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']", 'null': 'True', 'blank': 'True'}),
            'estado_credito': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha_final': ('django.db.models.fields.DateField', [], {}),
            'fecha_inicial': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero_cuotas': ('django.db.models.fields.IntegerField', [], {}),
            'proveedor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Proveedor']", 'null': 'True', 'blank': 'True'}),
            'saldo_capital': ('django.db.models.fields.FloatField', [], {}),
            'tipo_credito': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'ventas.cabeceradocumento': {
            'Meta': {'object_name': 'CabeceraDocumento'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']"}),
            'credito': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['creditos.Credito']", 'null': 'True', 'blank': 'True'}),
            'fecha_proceso': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_valor': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'proveedor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Proveedor']"}),
            'serie': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'tipo_documento': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'tipo_pago': ('django.db.models.fields.CharField', [], {'default': "u'Co'", 'max_length': '2'}),
            'total': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'ventas.detalledocumento': {
            'Meta': {'object_name': 'DetalleDocumento'},
            'cabecera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ventas.CabeceraDocumento']"}),
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio': ('django.db.models.fields.FloatField', [], {}),
            'precio_producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacenes.PrecioProducto']", 'null': 'True', 'blank': 'True'}),
            'producto_almacen': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacenes.ProductoAlmacen']"})
        }
    }

    complete_apps = ['ventas']