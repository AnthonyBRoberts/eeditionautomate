from signup.models import SimpleSubscriber, Product, Communication
from django.db import models
from django.contrib import admin
from django.contrib.admin import site, ModelAdmin
import models

class SimpleSubscriberAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User information', {'fields': ['name', 'address', 'city', 'state', 'zipcode', 'email',]}),
        ('system information', {'fields': ['date_created', 'sub_startdate', 'sub_type',], 'classes': ['collapse']}),
    ]
    list_display = ('name', 'email', 'address', 'city', 'state', 'zipcode')
    list_filter = ['sub_type',]
    search_fields = ['name', 'email',]
    date_hierarchy = 'date_created'

class CommonMedia:
  js = (
    'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
    '/appmedia/admin/js/editor.js',
  )
  css = {
    'all': ('/appmedia/admin/css/editor.css',),
  }

class CommunicationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Message details', {'fields': ['comm_name', 'comm_message', 'comm_active',]}),
        ('Message scheduling', {'fields': ['send_now', 'comm_schedule', 'days',]}),
    ]
    list_display  = ('comm_name', 'comm_active')
    search_fields = ['comm_name',]
    #js = ('/tinymce/jscripts/tiny_mce/tiny_mce.js', '/appmedia/admin/js/textareas.js')
    #formfield_overrides = {
        #models.CharField: {'widget': CommonMedia},
    #}

admin.site.register(models.Communication,
    list_display  = ('comm_name', 'comm_message', 'comm_active'),
    search_fields = ['comm_name',],
    #js = ('/tinymce/jscripts/tiny_mce/tiny_mce.js', '/appmedia/admin/js/textareas.js',)
    Media = CommonMedia,
)

#admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Product)
#admin.site.register(GetPayment)
#admin.site.register(Communication, CommunicationAdmin)
admin.site.register(SimpleSubscriber, SimpleSubscriberAdmin)


