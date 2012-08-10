from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^signup/', include('signup.urls')),
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^uploads/*', 'serve'), 
)
urlpatterns += staticfiles_urlpatterns()
