from signup.models import SimpleSubscriber, Product, Communication, Publisher, FileUploader
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

class ProductAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):            
        if not request.user.is_superuser:
            kwargs['fields'] = ['product_type', 'product_description', 'product_cost', 'product_active', 'duration', 'duration_type',]
        else:
            kwargs['fields'] = ['product_type', 'product_description', 'product_cost', 'product_active', 'duration', 'duration_type', 'publisher',]
        return super(ProductAdmin, self).get_form(request, obj, **kwargs)

    def queryset(self, request):
        if request.user.is_superuser:
            return Product.objects.all()
        return Product.objects.filter(publisher=request.user)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.publisher = Publisher.objects.get(id = request.user.id)
        obj.save()


class FileUploaderAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):            
        if not request.user.is_superuser:
            kwargs['fields'] = ['title', 'file',]
        else:
            kwargs['fields'] = ['title', 'file', 'publisher',]
        return super(FileUploaderAdmin, self).get_form(request, obj, **kwargs)

    def queryset(self, request):
        if request.user.is_superuser:
            return FileUploader.objects.all()
        return FileUploader.objects.filter(publisher=request.user)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.publisher = Publisher.objects.get(id = request.user.id)
        obj.save()
"""
    def download_file(request):
        with open('home/aroberts/webapps/eeditionautomate/eeditionautomate/media/uploads/') as file:
            response = HttpResponse(file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=
"""


class SimpleSubscriberAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'email', 'sub_type')
    list_filter = ['sub_type',]
    search_fields = ['last_name', 'email',]
    date_hierarchy = 'date_created'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "sub_type":
            subtype = Product.objects.all()
            if not request.user.is_superuser:
                kwargs["queryset"] = subtype.filter(publisher=request.user)
            else:
                kwargs["queryset"] = subtype
        return super(SimpleSubscriberAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_form(self, request, obj=None, **kwargs):
        if not request.user.is_superuser:
            kwargs['fields'] = ['first_name', 'last_name', 'username', 'password', 'address', 'city', 'state', 'zipcode', 'email', 'date_created', 'sub_startdate', 'sub_type',]
        else:
            kwargs['fields'] = ['first_name', 'last_name', 'username', 'password', 'address', 'city', 'state', 'zipcode', 'email', 'date_created', 'sub_startdate', 'sub_type', 'publisher',]

        return super(SimpleSubscriberAdmin, self).get_form(request, obj, **kwargs)

    def queryset(self, request):
        if request.user.is_superuser:
            return SimpleSubscriber.objects.all()
        return SimpleSubscriber.objects.filter(publisher=request.user)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.publisher = Publisher.objects.get(id = request.user.id)
        obj.save()

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(SimpleSubscriberAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.publisher.id:
            return False
        return True


class CommunicationAdmin(admin.ModelAdmin):
    
    list_display  = ('publisher', 'comm_name', 'comm_active')
    search_fields = ['comm_name',]

    def get_form(self, request, obj=None, **kwargs):            
        if not request.user.is_superuser:
            kwargs['fields'] = ['comm_name', 'comm_message', 'comm_active', 'send_now', 'comm_schedule', 'days', 'sub_status',]
        else:
            kwargs['fields'] = ['comm_name', 'comm_message', 'comm_active', 'send_now', 'comm_schedule', 'days', 'sub_status', 'publisher',]
        return super(CommunicationAdmin, self).get_form(request, obj, **kwargs)
    
    def queryset(self, request):
        if request.user.is_superuser:
            return Communication.objects.all()
        return Communication.objects.filter(publisher=request.user)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.publisher = Publisher.objects.get(id = request.user.id)
        obj.save()


admin.site.register(Product, ProductAdmin)
admin.site.register(Communication, CommunicationAdmin)
admin.site.register(SimpleSubscriber, SimpleSubscriberAdmin)
admin.site.register(Publisher)
admin.site.register(FileUploader, FileUploaderAdmin)


