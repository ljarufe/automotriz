# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Marca'
        db.create_table(u'almacenes_marca', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('abreviatura', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'almacenes', ['Marca'])

        # Adding model 'Unidad'
        db.create_table(u'almacenes_unidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('abreviatura', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'almacenes', ['Unidad'])

        # Adding model 'Producto'
        db.create_table(u'almacenes_producto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('abreviatura', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('unidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['almacenes.Unidad'], null=True, blank=True)),
        ))
        db.send_create_signal(u'almacenes', ['Producto'])

        # Adding model 'PrecioProducto'
        db.create_table(u'almacenes_precioproducto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('precio', self.gf('django.db.models.fields.FloatField')()),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['almacenes.Producto'])),
        ))
        db.send_create_signal(u'almacenes', ['PrecioProducto'])

        # Adding model 'Sucursal'
        db.create_table(u'almacenes_sucursal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
        ))
        db.send_create_signal(u'almacenes', ['Sucursal'])

        # Adding model 'Almacen'
        db.create_table(u'almacenes_almacen', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sucursal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['almacenes.Sucursal'])),
        ))
        db.send_create_signal(u'almacenes', ['Almacen'])

        # Adding model 'ProductoAlmacen'
        db.create_table(u'almacenes_productoalmacen', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['almacenes.Producto'])),
            ('almacen', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['almacenes.Almacen'])),
            ('unidades', self.gf('django.db.models.fields.FloatField')()),
            ('fecha_ultimo_movimiento', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fecha_vencimiento', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'almacenes', ['ProductoAlmacen'])


    def backwards(self, orm):
        # Deleting model 'Marca'
        db.delete_table(u'almacenes_marca')

        # Deleting model 'Unidad'
        db.delete_table(u'almacenes_unidad')

        # Deleting model 'Producto'
        db.delete_table(u'almacenes_producto')

        # Deleting model 'PrecioProducto'
        db.delete_table(u'almacenes_precioproducto')

        # Deleting model 'Sucursal'
        db.delete_table(u'almacenes_sucursal')

        # Deleting model 'Almacen'
        db.delete_table(u'almacenes_almacen')

        # Deleting model 'ProductoAlmacen'
        db.delete_table(u'almacenes_productoalmacen')


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
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacenes.Producto']"})
        },
        u'almacenes.producto': {
            'Meta': {'object_name': 'Producto'},
            'abreviatura': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['almacenes.Unidad']", 'null': 'True', 'blank': 'True'})
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