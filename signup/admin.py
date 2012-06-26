from signup.models import SimpleSubscriber, Product, Communication, Publisher
from django.db import models
from django.contrib import admin
from django.contrib.admin import site, ModelAdmin
import models

class PublisherAdmin(admin.ModelAdmin):
    #stuff here??
    def queryset(self, request):
        if request.user.is_superuser:
            return Model.objects.all()
        return Model.objects.filter(edition=request.user.get_profile().fieldnameicreate)

class SimpleSubscriberAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User information', {'fields': ['name', 'address', 'city', 'state', 'zipcode', 'email',]}),
        ('system information', {'fields': ['date_created', 'sub_startdate', 'sub_type', ], 'classes': ['collapse']}),
    ]
    
    exclude = ('publisher',)
    list_display = ('name', 'email', 'address', 'city', 'zipcode')
    list_filter = ['sub_type',]
    search_fields = ['name', 'email',]
    date_hierarchy = 'date_created'
    
    def queryset(self, request):
        if request.user.is_superuser:
            return SimpleSubscriber.objects.all()
        return SimpleSubscriber.objects.filter(publisher=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.publisher = request.user
        obj.save()


    def has_change_permission(self, request, obj=None):
        has_class_permission = super(SimpleSubscriberAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.publisher.id:
            return False
        return True


class CommunicationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Message details', {'fields': ['comm_name', 'comm_message', 'comm_active',]}),
        ('Message scheduling', {'fields': ['send_now', 'comm_schedule', 'days', 'sub_status',]}),
    ]
    list_display  = ('comm_name', 'comm_active')
    search_fields = ['comm_name',]
    
    def queryset(self, request):
        if request.user.is_superuser:
            return Communication.objects.all()
        return Communication.objects.filter(publisher=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.publisher = request.user
        obj.save()


class CommonMedia:
  js = (
    'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
    '/appmedia/admin/js/editor.js',
  )
  css = {
    'all': ('/appmedia/admin/css/editor.css',),
  }


admin.site.register(Product)
admin.site.register(Communication, CommunicationAdmin)
admin.site.register(SimpleSubscriber, SimpleSubscriberAdmin)
admin.site.register(Publisher)


