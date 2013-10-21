# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoMoneda'
        db.create_table('common_tipomoneda', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('abreviatura', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal('common', ['TipoMoneda'])


    def backwards(self, orm):
        # Deleting model 'TipoMoneda'
        db.delete_table('common_tipomoneda')


    models = {
        'common.cambiomoneda': {
            'Meta': {'object_name': 'CambioMoneda'},
            'cambio': ('django.db.models.fields.FloatField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'common.constantes': {
            'Meta': {'object_name': 'Constantes'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'valor': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'common.tipomoneda': {
            'Meta': {'object_name': 'TipoMoneda'},
            'abreviatura': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['common']