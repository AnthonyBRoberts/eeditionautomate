from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^signup/$', 'signup.views.select_product', name='select_product'),
    url(r'^signup/(?P<product_id>\d+/)$', 'signup.views.subscriber_signup', name='subscriber_signup'),
#    url(r'^signup/(?P<poll_id>\d+)/results/$', 'signup.views.create'),
    url(r'^admin/', include(admin.site.urls)),
)
