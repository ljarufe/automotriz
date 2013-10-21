# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoDocumento'
        db.create_table(u'clientes_tipodocumento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('abreviatura', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal(u'clientes', ['TipoDocumento'])

        # Adding model 'Cliente'
        db.create_table(u'clientes_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo_entidad', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('tipo_documento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.TipoDocumento'])),
            ('numero_documento', self.gf('django.db.models.fields.CharField')(max_length=11, null=True, blank=True)),
            ('tipo_persona', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('apellido_paterno', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('apellido_materno', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('nombres', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('razon_social', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('direccion_extra', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('telefono_fijo', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
            ('telefono_celular', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
        ))
        db.send_create_signal(u'clientes', ['Cliente'])

        # Adding model 'Proveedor'
        db.create_table(u'clientes_proveedor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo_entidad', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('tipo_documento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.TipoDocumento'])),
            ('numero_documento', self.gf('django.db.models.fields.CharField')(max_length=11, null=True, blank=True)),
            ('tipo_persona', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('apellido_paterno', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('apellido_materno', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('nombres', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('razon_social', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('direccion_extra', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('telefono_fijo', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
            ('telefono_celular', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
        ))
        db.send_create_signal(u'clientes', ['Proveedor'])

        # Adding model 'Socio'
        db.create_table(u'clientes_socio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo_entidad', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('tipo_documento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.TipoDocumento'])),
            ('numero_documento', self.gf('django.db.models.fields.CharField')(max_length=11, null=True, blank=True)),
            ('tipo_persona', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('apellido_paterno', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('apellido_materno', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('nombres', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('razon_social', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('direccion_extra', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('telefono_fijo', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
            ('telefono_celular', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
        ))
        db.send_create_signal(u'clientes', ['Socio'])


    def backwards(self, orm):
        # Deleting model 'TipoDocumento'
        db.delete_table(u'clientes_tipodocumento')

        # Deleting model 'Cliente'
        db.delete_table(u'clientes_cliente')

        # Deleting model 'Proveedor'
        db.delete_table(u'clientes_proveedor')

        # Deleting model 'Socio'
        db.delete_table(u'clientes_socio')


    models = {
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'apellido_materno': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'apellido_paterno': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'codigo_entidad': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'direccion_extra': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
        u'clientes.socio': {
            'Meta': {'object_name': 'Socio'},
            'apellido_materno': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'apellido_paterno': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'codigo_entidad': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'direccion_extra': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
        }
    }

    complete_apps = ['clientes']