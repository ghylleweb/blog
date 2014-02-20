# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ApiLink.callback_url'
        db.add_column(u'apis_apilink', 'callback_url',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ApiLink.callback_url'
        db.delete_column(u'apis_apilink', 'callback_url')


    models = {
        u'apis.apilink': {
            'Meta': {'object_name': 'ApiLink'},
            'access_token': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'access_token_secret': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'api_key': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'api_secret': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'callback_url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '75'})
        }
    }

    complete_apps = ['apis']