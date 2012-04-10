from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from django.contrib import admin
from eeditionautomate.signup.models import Product, Subscriber, GetPayment
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^signup/$', 'signup.views.select_product', name='select_product'),
    url(r'^signup/(?P<product_id>\d+)/$', 'signup.views.subscriber_signup', name='subscriber_signup'), 
    url(r'^signup/(?P<product_id>\d+)/thankyou/$', 'signup.views.select_product', name='select_product'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
)
# /login/<user>/
urlpatterns += staticfiles_urlpatterns()
