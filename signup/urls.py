from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from django.contrib import admin
from django import forms
from eeditionautomate.signup.models import Product, Publisher
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns, include, url
admin.autodiscover()

urlpatterns = patterns('signup.views',
    url(r'^(?P<publisher_id>\d+)/$', 'select_product', name='select_product'),
    url(r'^(?P<publisher_id>\d+)/(?P<product_id>\d+)/$', 'subscriber_signup', name='subscriber_signup'), 
    url(r'^(?P<publisher_id>\d+)/(?P<product_id>\d+)/paypal/$', 'paypal', name='paypal'),
    (r'^something/hard/to/guess/', include('paypal.standard.ipn.urls')),
)

urlpatterns += staticfiles_urlpatterns()

