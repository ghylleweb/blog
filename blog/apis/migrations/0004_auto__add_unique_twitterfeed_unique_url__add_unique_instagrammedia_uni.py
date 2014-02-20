# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'TwitterFeed', fields ['unique_url']
        db.create_unique(u'apis_twitterfeed', ['unique_url'])

        # Adding unique constraint on 'InstagramMedia', fields ['unique_url']
        db.create_unique(u'apis_instagrammedia', ['unique_url'])

        # Adding unique constraint on 'StravaActivity', fields ['unique_url']
        db.create_unique(u'apis_stravaactivity', ['unique_url'])

        # Adding unique constraint on 'FoursquareCheckin', fields ['unique_url']
        db.create_unique(u'apis_foursquarecheckin', ['unique_url'])


    def backwards(self, orm):
        # Removing unique constraint on 'FoursquareCheckin', fields ['unique_url']
        db.delete_unique(u'apis_foursquarecheckin', ['unique_url'])

        # Removing unique constraint on 'StravaActivity', fields ['unique_url']
        db.delete_unique(u'apis_stravaactivity', ['unique_url'])

        # Removing unique constraint on 'InstagramMedia', fields ['unique_url']
        db.delete_unique(u'apis_instagrammedia', ['unique_url'])

        # Removing unique constraint on 'TwitterFeed', fields ['unique_url']
        db.delete_unique(u'apis_twitterfeed', ['unique_url'])


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
            'unique_url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
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
            'unique_url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'video_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'apis.stravaactivity': {
            'Meta': {'object_name': 'StravaActivity'},
            'activity_type': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'avg_speed': ('django.db.models.fields.FloatField', [], {}),
            'avg_temp': ('django.db.models.fields.FloatField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unique_url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'})
        },
        u'apis.twitterfeed': {
            'Meta': {'object_name': 'TwitterFeed'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tweet_lat': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'tweet_lng': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'tweet_text': ('django.db.models.fields.TextField', [], {}),
            'unique_url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['apis']