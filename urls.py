from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from django.contrib import admin
from django import forms
#from eeditionautomate.signup.models import Product, Publisher
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^signup/', include('signup.urls')),
    url(r'^admin/', include(admin.site.urls)), 
    #url(r'^paypal/(?P<publisher_id>\d+)/(?P<product_id>\d+)/$', 'paypal', name='paypal'),
)
#urlpatterns = patterns('',
    #url(r'^signup/(P<publisher_id>\d+/submit$', ProductFormPreview(ProductForm)), 
    #url(r'^signup/$', 'signup.views.select_product', name='select_product'),
    #url(r'^signup/(?P<product_id>\d+)/$', 'signup.views.subscriber_signup', name='subscriber_signup'),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
#)
# /login/<user>/
#urlpatterns += staticfiles_urlpatterns()
#urlpatterns += patterns('',
#(r'^something/hard/to/guess/', include('paypal.standard.ipn.urls'))#,enewsautomation.dyndns-mail.com
#) 
