# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Publisher'
        db.create_table('signup_publisher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=55)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('signup', ['Publisher'])

        # Adding model 'PublisherUserProfile'
        db.create_table('signup_publisheruserprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['signup.Publisher'], unique=True)),
        ))
        db.send_create_signal('signup', ['PublisherUserProfile'])

        # Adding model 'Product'
        db.create_table('signup_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('product_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('product_description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('product_cost', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('product_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('duration', self.gf('django.db.models.fields.IntegerField')()),
            ('duration_type', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('signup', ['Product'])

        # Adding model 'Subscription'
        db.create_table('signup_subscription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['signup.Product'])),
            ('starts', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('signup', ['Subscription'])

        # Adding model 'SimpleSubscriber'
        db.create_table('signup_simplesubscriber', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('date_created', self.gf('django.db.models.fields.DateField')(null=True)),
            ('sub_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['signup.Product'])),
            ('sub_startdate', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('signup', ['SimpleSubscriber'])

        # Adding model 'Communication'
        db.create_table('signup_communication', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('comm_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('comm_message', self.gf('ckeditor.fields.HTMLField')()),
            ('comm_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('send_now', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('comm_schedule', self.gf('django.db.models.fields.DateTimeField')()),
            ('days', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('sub_status', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('signup', ['Communication'])


    def backwards(self, orm):
        # Deleting model 'Publisher'
        db.delete_table('signup_publisher')

        # Deleting model 'PublisherUserProfile'
        db.delete_table('signup_publisheruserprofile')

        # Deleting model 'Product'
        db.delete_table('signup_product')

        # Deleting model 'Subscription'
        db.delete_table('signup_subscription')

        # Deleting model 'SimpleSubscriber'
        db.delete_table('signup_simplesubscriber')

        # Deleting model 'Communication'
        db.delete_table('signup_communication')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'signup.communication': {
            'Meta': {'object_name': 'Communication'},
            'comm_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comm_message': ('ckeditor.fields.HTMLField', [], {}),
            'comm_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'comm_schedule': ('django.db.models.fields.DateTimeField', [], {}),
            'days': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'send_now': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sub_status': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'signup.product': {
            'Meta': {'object_name': 'Product'},
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            'duration_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'product_cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'product_description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'product_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'signup.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'signup.publisheruserprofile': {
            'Meta': {'object_name': 'PublisherUserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['signup.Publisher']", 'unique': 'True'})
        },
        'signup.simplesubscriber': {
            'Meta': {'object_name': 'SimpleSubscriber'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date_created': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'sub_startdate': ('django.db.models.fields.DateField', [], {}),
            'sub_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['signup.Product']"}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '9'})
        },
        'signup.subscription': {
            'Meta': {'object_name': 'Subscription'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['signup.Product']"}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'starts': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['signup']