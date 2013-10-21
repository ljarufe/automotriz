# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PrecioProducto.tipo_precio'
        db.add_column(u'almacenes_precioproducto', 'tipo_precio',
                      self.gf('django.db.models.fields.CharField')(default='C', max_length=1),
                      keep_default=False)

        # Adding field 'Producto.medida'
        db.add_column(u'almacenes_producto', 'medida',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Producto.aro'
        db.add_column(u'almacenes_producto', 'aro',
                      self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Producto.pr'
        db.add_column(u'almacenes_producto', 'pr',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Producto.uso'
        db.add_column(u'almacenes_producto', 'uso',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PrecioProducto.tipo_precio'
        db.delete_column(u'almacenes_precioproducto', 'tipo_precio')

        # Deleting field 'Producto.medida'
        db.delete_column(u'almacenes_producto', 'medida')

        # Deleting field 'Producto.aro'
        db.delete_column(u'almacenes_producto', 'aro')

        # Deleting field 'Producto.pr'
        db.delete_column(u'almacenes_producto', 'pr')

        # Deleting field 'Producto.uso'
        db.delete_column(u'almacenes_producto', 'uso')


    models = {
        u'almacenes.almacen': {
            'Meta': {'object_name': 'Almacen'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'productos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['almacenes.Producto']", 'through': u"orm['almacenes.ProductoAlmacen']", 'symmetrical': 'False'}),
            'sucursal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacenes.Sucursal']"})
        },
        u'almacenes.marca': {
            'Meta': {'object_name': 'Marca'},
            'abreviatura': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'almacenes.precioproducto': {
            'Meta': {'object_name': 'PrecioProducto'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio': ('django.db.models.fields.FloatField', [], {}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacenes.Producto']"}),
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
            'fecha_vencimiento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
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
        }
    }

    complete_apps = ['almacenes']