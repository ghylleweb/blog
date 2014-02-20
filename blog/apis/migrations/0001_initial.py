# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ApiLink'
        db.create_table(u'apis_apilink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=75)),
            ('api_key', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('api_secret', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('access_token', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('access_token_secret', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'apis', ['ApiLink'])


    def backwards(self, orm):
        # Deleting model 'ApiLink'
        db.delete_table(u'apis_apilink')


    models = {
        u'apis.apilink': {
            'Meta': {'object_name': 'ApiLink'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'access_token_secret': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'api_key': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'api_secret': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '75'})
        }
    }

    complete_apps = ['apis']