from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^signup/', include('signup.urls')),
    url(r'^admin/', include(admin.site.urls)),  
)

