# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'SimpleSubscriber.id'
        db.delete_column('signup_simplesubscriber', 'id')

        # Deleting field 'SimpleSubscriber.name'
        db.delete_column('signup_simplesubscriber', 'name')

        # Deleting field 'SimpleSubscriber.email'
        db.delete_column('signup_simplesubscriber', 'email')

        # Adding field 'SimpleSubscriber.user_ptr'
        db.add_column('signup_simplesubscriber', 'user_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['auth.User'], unique=True, primary_key=True),
                      keep_default=False)


        # Changing field 'SimpleSubscriber.publisher'
        db.alter_column('signup_simplesubscriber', 'publisher_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['signup.Publisher']))

        # Changing field 'Product.publisher'
        db.alter_column('signup_product', 'publisher_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['signup.Publisher']))
        # Deleting field 'Publisher.start_date'
        db.delete_column('signup_publisher', 'start_date')

        # Deleting field 'Publisher.email'
        db.delete_column('signup_publisher', 'email')

        # Deleting field 'Publisher.name'
        db.delete_column('signup_publisher', 'name')

        # Deleting field 'Publisher.id'
        db.delete_column('signup_publisher', 'id')

        # Adding field 'Publisher.user_ptr'
        db.add_column('signup_publisher', 'user_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['auth.User'], unique=True, primary_key=True),
                      keep_default=False)


        # Changing field 'Communication.publisher'
        db.alter_column('signup_communication', 'publisher_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['signup.Publisher']))

        # Changing field 'Subscription.publisher'
        db.alter_column('signup_subscription', 'publisher_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['signup.Publisher']))

    def backwards(self, orm):
        # Adding field 'SimpleSubscriber.id'
        db.add_column('signup_simplesubscriber', 'id',
                      self.gf('django.db.models.fields.AutoField')(default=1, primary_key=True),
                      keep_default=False)

        # Adding field 'SimpleSubscriber.name'
        db.add_column('signup_simplesubscriber', 'name',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=255),
                      keep_default=False)

        # Adding field 'SimpleSubscriber.email'
        db.add_column('signup_simplesubscriber', 'email',
                      self.gf('django.db.models.fields.EmailField')(default=1, max_length=75),
                      keep_default=False)

        # Deleting field 'SimpleSubscriber.user_ptr'
        db.delete_column('signup_simplesubscriber', 'user_ptr_id')


        # Changing field 'SimpleSubscriber.publisher'
        db.alter_column('signup_simplesubscriber', 'publisher_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Product.publisher'
        db.alter_column('signup_product', 'publisher_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))
        # Adding field 'Publisher.start_date'
        db.add_column('signup_publisher', 'start_date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 7, 18, 0, 0)),
                      keep_default=False)

        # Adding field 'Publisher.email'
        db.add_column('signup_publisher', 'email',
                      self.gf('django.db.models.fields.EmailField')(default=1, max_length=75),
                      keep_default=False)

        # Adding field 'Publisher.name'
        db.add_column('signup_publisher', 'name',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=55),
                      keep_default=False)

        # Adding field 'Publisher.id'
        db.add_column('signup_publisher', 'id',
                      self.gf('django.db.models.fields.AutoField')(default=1, primary_key=True),
                      keep_default=False)

        # Deleting field 'Publisher.user_ptr'
        db.delete_column('signup_publisher', 'user_ptr_id')


        # Changing field 'Communication.publisher'
        db.alter_column('signup_communication', 'publisher_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'Subscription.publisher'
        db.alter_column('signup_subscription', 'publisher_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

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
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['signup.Publisher']"}),
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
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['signup.Publisher']"})
        },
        'signup.publisher': {
            'Meta': {'object_name': 'Publisher', '_ormbases': ['auth.User']},
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'signup.publisheruserprofile': {
            'Meta': {'object_name': 'PublisherUserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['signup.Publisher']", 'unique': 'True'})
        },
        'signup.simplesubscriber': {
            'Meta': {'object_name': 'SimpleSubscriber', '_ormbases': ['auth.User']},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date_created': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['signup.Publisher']"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'sub_startdate': ('django.db.models.fields.DateField', [], {}),
            'sub_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['signup.Product']"}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '9'})
        },
        'signup.subscription': {
            'Meta': {'object_name': 'Subscription'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['signup.Product']"}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['signup.Publisher']"}),
            'starts': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['signup']