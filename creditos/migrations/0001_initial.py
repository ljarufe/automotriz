# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Credito'
        db.create_table(u'creditos_credito', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cliente'], null=True, blank=True)),
            ('proveedor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Proveedor'], null=True, blank=True)),
            ('tipo_credito', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('capital_pactado', self.gf('django.db.models.fields.FloatField')()),
            ('saldo_capital', self.gf('django.db.models.fields.FloatField')()),
            ('numero_cuotas', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha_inicial', self.gf('django.db.models.fields.DateField')()),
            ('fecha_final', self.gf('django.db.models.fields.DateField')()),
            ('estado_credito', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'creditos', ['Credito'])

        # Adding model 'PlanPago'
        db.create_table(u'creditos_planpago', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('credito', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['creditos.Credito'])),
            ('numero_cuota', self.gf('django.db.models.fields.IntegerField')()),
            ('estado_cuota', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('capital_pactado', self.gf('django.db.models.fields.FloatField')()),
            ('capital_pagado', self.gf('django.db.models.fields.FloatField')()),
            ('fecha_vencimiento', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'creditos', ['PlanPago'])


    def backwards(self, orm):
        # Deleting model 'Credito'
        db.delete_table(u'creditos_credito')

        # Deleting model 'PlanPago'
        db.delete_table(u'creditos_planpago')


    models = {
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
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
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
        u'creditos.planpago': {
            'Meta': {'object_name': 'PlanPago'},
            'capital_pactado': ('django.db.models.fields.FloatField', [], {}),
            'capital_pagado': ('django.db.models.fields.FloatField', [], {}),
            'credito': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['creditos.Credito']"}),
            'estado_cuota': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha_vencimiento': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero_cuota': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['creditos']