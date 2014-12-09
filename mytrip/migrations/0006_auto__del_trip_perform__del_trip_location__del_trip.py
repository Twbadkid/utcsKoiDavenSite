# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Trip_Perform'
        db.delete_table(u'mytrip_trip_perform')

        # Deleting model 'Trip_Location'
        db.delete_table(u'mytrip_trip_location')

        # Deleting model 'Trip'
        db.delete_table(u'mytrip_trip')


    def backwards(self, orm):
        # Adding model 'Trip_Perform'
        db.create_table(u'mytrip_trip_perform', (
            ('tripid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mytrip.Trip'], primary_key=True)),
            ('data', self.gf('django.db.models.fields.TextField')()),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('permission', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'mytrip', ['Trip_Perform'])

        # Adding model 'Trip_Location'
        db.create_table(u'mytrip_trip_location', (
            ('lid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mytrip.Local'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('no', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.FilePathField')(path='/srv/www/pmem/media', max_length=100, recursive=True)),
            ('dtime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('tid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mytrip.Trip'])),
        ))
        db.send_create_signal(u'mytrip', ['Trip_Location'])

        # Adding model 'Trip'
        db.create_table(u'mytrip_trip', (
            ('trip_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('trip_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('trip_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mytrip.User'])),
        ))
        db.send_create_signal(u'mytrip', ['Trip'])


    models = {
        u'mytrip.local': {
            'Meta': {'object_name': 'Local', 'db_table': "'local'"},
            'latitude': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '8'}),
            'local_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'local_name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '12', 'decimal_places': '8'})
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