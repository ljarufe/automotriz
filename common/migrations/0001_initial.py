# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Constantes'
        db.create_table('common_constantes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('valor', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('common', ['Constantes'])

        # Adding model 'CambioMoneda'
        db.create_table('common_cambiomoneda', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
            ('cambio', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('common', ['CambioMoneda'])


    def backwards(self, orm):
        # Deleting model 'Constantes'
        db.delete_table('common_constantes')

        # Deleting model 'CambioMoneda'
        db.delete_table('common_cambiomoneda')


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
        }
    }

    complete_apps = ['common']