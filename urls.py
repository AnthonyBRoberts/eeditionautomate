from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^signup/$', 'signup.views.index', name='home'),
#    url(r'^signup/(?P<poll_id>\d+)/$', 'signup.views.detail'),
#    url(r'^signup/(?P<poll_id>\d+)/results/$', 'signup.views.create'),
    url(r'^admin/', include(admin.site.urls)),
)
