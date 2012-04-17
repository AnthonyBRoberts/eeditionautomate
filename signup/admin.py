from signup.models import Subscriber, SimpleSubscriber
from signup.models import Product
from signup.models import GetPayment
from signup.models import Communication
from django.contrib import admin

class SubscriberAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User information',               {'fields': ['first_name', 'last_name', 'email', 'username', 'password', 'sub_type']}),
        ('custom information', {'fields': ['date_created', 'address'], 'classes': ['collapse']}),
    ]
    list_display = ('first_name', 'last_name', 'email', 'sub_type')
    list_filter = ['sub_type']
    search_fields = ['last_name', 'email']
    date_hierarchy = 'date_created'


admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Product)
admin.site.register(GetPayment)
admin.site.register(Communication)
admin.site.register(SimpleSubscriber)

class CommonMedia:
  js = (
    'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
    '/appmedia/admin/js/editor.js',
  )
  css = {
    'all': ('/appmedia/admin/css/editor.css',),
  }
