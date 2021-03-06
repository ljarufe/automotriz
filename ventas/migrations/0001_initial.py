# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CabeceraDocumento'
        db.create_table('ventas_cabeceradocumento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('serie', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('proveedor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Proveedor'])),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cliente'])),
            ('fecha_valor', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
            ('fecha_proceso', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('total', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('observaciones', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('ventas', ['CabeceraDocumento'])

        # Adding model 'DetalleDocumento'
        db.create_table('ventas_detalledocumento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cabecera', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ventas.CabeceraDocumento'])),
            ('cantidad', self.gf('django.db.models.fields.FloatField')()),
            ('producto_almacen', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['almacenes.ProductoAlmacen'])),
            ('precio_producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['almacenes.PrecioProducto'], null=True, blank=True)),
            ('precio', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('ventas', ['DetalleDocumento'])


    def backwards(self, orm):
        # Deleting model 'CabeceraDocumento'
        db.delete_table('ventas_cabeceradocumento')

        # Deleting model 'DetalleDocumento'
        db.delete_table('ventas_detalledocumento')


    models = {
        'almacenes.almacen': {
            'Meta': {'object_name': 'Almacen'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['almacenes.Producto']", 'through': "orm['almacenes.ProductoAlmacen']", 'symmetrical': 'False'}),
            'sucursal': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['almacenes.Sucursal']"})
        },
        'almacenes.precioproducto': {
            'Meta': {'object_name': 'PrecioProducto'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio': ('django.db.models.fields.FloatField', [], {}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['almacenes.Producto']"}),
            'tipo_moneda': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['common.TipoMoneda']"}),
            'tipo_precio': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'almacenes.producto': {
            'Meta': {'object_name': 'Producto'},
            'abreviatura': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'aro': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medida': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'pr': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'unidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['almacenes.Unidad']", 'null': 'True', 'blank': 'True'}),
            'uso': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        'almacenes.productoalmacen': {
            'Meta': {'object_name': 'ProductoAlmacen'},
            'almacen': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['almacenes.Almacen']"}),
            'fecha_ultimo_movimiento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['almacenes.Producto']"}),
            'unidades': ('django.db.models.fields.FloatField', [], {})
        },
        'almacenes.sucursal': {
            'Meta': {'object_name': 'Sucursal'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        'almacenes.unidad': {
            'Meta': {'object_name': 'Unidad'},
            'abreviatura': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'apellido_materno': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'apellido_paterno': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'codigo_entidad': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'direccion_extra': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'numero_documento': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'razon_social': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telefono_celular': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'telefono_fijo': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'tipo_documento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clientes.TipoDocumento']"}),
            'tipo_persona': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'clientes.proveedor': {
            'Meta': {'object_name': 'Proveedor'},
            'apellido_materno': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'apellido_paterno': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'codigo_entidad': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'direccion_extra': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'numero_documento': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'razon_social': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telefono_celular': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'telefono_fijo': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'tipo_documento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clientes.TipoDocumento']"}),
            'tipo_persona': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'clientes.tipodocumento': {
            'Meta': {'object_name': 'TipoDocumento'},
            'abreviatura': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'common.tipomoneda': {
            'Meta': {'object_name': 'TipoMoneda'},
            'abreviatura': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'ventas.cabeceradocumento': {
            'Meta': {'object_name': 'CabeceraDocumento'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clientes.Cliente']"}),
            'fecha_proceso': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_valor': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'proveedor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clientes.Proveedor']"}),
            'serie': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'total': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        'ventas.detalledocumento': {
            'Meta': {'object_name': 'DetalleDocumento'},
            'cabecera': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ventas.CabeceraDocumento']"}),
            'cantidad': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio': ('django.db.models.fields.FloatField', [], {}),
            'precio_producto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['almacenes.PrecioProducto']", 'null': 'True', 'blank': 'True'}),
            'producto_almacen': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['almacenes.ProductoAlmacen']"})
        }
    }

    complete_apps = ['ventas']