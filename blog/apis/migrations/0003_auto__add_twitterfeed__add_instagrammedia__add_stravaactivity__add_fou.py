# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TwitterFeed'
        db.create_table(u'apis_twitterfeed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unique_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('tweet_text', self.gf('django.db.models.fields.TextField')()),
            ('tweet_lat', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('tweet_lng', self.gf('django.db.models.fields.FloatField')(blank=True)),
        ))
        db.send_create_signal(u'apis', ['TwitterFeed'])

        # Adding model 'InstagramMedia'
        db.create_table(u'apis_instagrammedia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unique_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('media_type', self.gf('django.db.models.fields.CharField')(default='pic', max_length=3)),
            ('caption', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('location_lat', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('location_lng', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('thumbnail', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('media_image', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('video_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'apis', ['InstagramMedia'])

        # Adding model 'StravaActivity'
        db.create_table(u'apis_stravaactivity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unique_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('activity_type', self.gf('django.db.models.fields.CharField')(default='C', max_length=1)),
            ('avg_temp', self.gf('django.db.models.fields.FloatField')()),
            ('avg_speed', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'apis', ['StravaActivity'])

        # Adding model 'FoursquareCheckin'
        db.create_table(u'apis_foursquarecheckin', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unique_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('venue_url', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('venue_name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('venue_lat', self.gf('django.db.models.fields.FloatField')()),
            ('venue_lng', self.gf('django.db.models.fields.FloatField')()),
            ('checkin_shout', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'apis', ['FoursquareCheckin'])


    def backwards(self, orm):
        # Deleting model 'TwitterFeed'
        db.delete_table(u'apis_twitterfeed')

        # Deleting model 'InstagramMedia'
        db.delete_table(u'apis_instagrammedia')

        # Deleting model 'StravaActivity'
        db.delete_table(u'apis_stravaactivity')

        # Deleting model 'FoursquareCheckin'
        db.delete_table(u'apis_foursquarecheckin')


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
        },
        u'apis.foursquarecheckin': {
            'Meta': {'object_name': 'FoursquareCheckin'},
            'checkin_shout': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unique_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'venue_lat': ('django.db.models.fields.FloatField', [], {}),
            'venue_lng': ('django.db.models.fields.FloatField', [], {}),
            'venue_name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'venue_url': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'apis.instagrammedia': {
            'Meta': {'object_name': 'InstagramMedia'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_lat': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'location_lng': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'media_image': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'media_type': ('django.db.models.fields.CharField', [], {'default': "'pic'", 'max_length': '3'}),
            'thumbnail': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'unique_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'apis.stravaactivity': {
            'Meta': {'object_name': 'StravaActivity'},
            'activity_type': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'avg_speed': ('django.db.models.fields.FloatField', [], {}),
            'avg_temp': ('django.db.models.fields.FloatField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unique_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'apis.twitterfeed': {
            'Meta': {'object_name': 'TwitterFeed'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tweet_lat': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'tweet_lng': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'tweet_text': ('django.db.models.fields.TextField', [], {}),
            'unique_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['apis']