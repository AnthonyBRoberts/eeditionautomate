from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from django.contrib import admin
from eeditionautomate.signup.models import Product, Subscriber, GetPayment
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns, include, url
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^signup/$', 'signup.views.select_product', name='select_product'),
    url(r'^signup/(?P<product_id>\d+)/$', 'signup.views.subscriber_signup', name='subscriber_signup'), 
    url(r'^signup/(?P<product_id>\d+)/thankyou/$', 'signup.views.thankyou', name='thankyou'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    #url(r'^$', 'cat.homepage.views.home', name='home'),
    url(r'^paypal/(?P<product_id>\d+)/$', 'signup.views.paypal', name='paypal'),
)
# /login/<user>/
urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
(r'^something/hard/to/guess/', include('paypal.standard.ipn.urls'))#,enewsautomation.dyndns-mail.com
) 
