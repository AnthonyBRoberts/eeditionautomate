from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from django.contrib import admin
from eeditionautomate.signup.models import Product, Subscriber, GetPayment
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^signup/$', 'signup.views.select_product', name='select_product'),
    url(r'^signup/(?P<product_id>\d+)/$', 'signup.views.subscriber_signup', name='subscriber_signup'),
    url(r'^signup/(?P<pk>\d+)/results/$', 
        DetailView.as_view(
            model=Subscriber,
            template_name='signup/thankyou.html'),
        name='signup_result'),
    url(r'^admin/', include(admin.site.urls)),
)
# /login/<user>/
