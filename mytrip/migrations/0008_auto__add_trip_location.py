# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Trip_Location'
        db.create_table(u'mytrip_trip_location', (
            ('no', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('tid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mytrip.Trip'])),
            ('photo', self.gf('django.db.models.fields.FilePathField')(path='/srv/www/pmem/media', max_length=100, recursive=True, blank=True)),
            ('lid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mytrip.Local'])),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('dtime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'mytrip', ['Trip_Location'])


    def backwards(self, orm):
        # Deleting model 'Trip_Location'
        db.delete_table(u'mytrip_trip_location')


    models = {
        u'mytrip.local': {
            'Meta': {'object_name': 'Local', 'db_table': "'local'"},
            'latitude': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '8'}),
            'local_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'local_name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '8'})
        },
        u'mytrip.trip': {
            'Meta': {'object_name': 'Trip'},
            'trip_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'trip_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'trip_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uid_id': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['mytrip.User']"})
        },
        u'mytrip.trip_location': {
            'Meta': {'object_name': 'Trip_Location'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'dtime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'lid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mytrip.Local']"}),
            'no': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.FilePathField', [], {'path': "'/srv/www/pmem/media'", 'max_length': '100', 'recursive': 'True', 'blank': 'True'}),
            'tid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mytrip.Trip']"})
        },
        u'mytrip.user': {
            'Meta': {'object_name': 'User'},
            'check_id': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'idnum': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['mytrip']