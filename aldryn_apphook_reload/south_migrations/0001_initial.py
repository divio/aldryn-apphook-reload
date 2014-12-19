# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UrlconfRevision'
        db.create_table(u'aldryn_apphook_reload_urlconfrevision', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('revision', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'aldryn_apphook_reload', ['UrlconfRevision'])


    def backwards(self, orm):
        # Deleting model 'UrlconfRevision'
        db.delete_table(u'aldryn_apphook_reload_urlconfrevision')


    models = {
        u'aldryn_apphook_reload.urlconfrevision': {
            'Meta': {'object_name': 'UrlconfRevision'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['aldryn_apphook_reload']