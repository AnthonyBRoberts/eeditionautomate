from signup.models import Subscriber
from signup.models import Product
from signup.models import GetPayment
from signup.models import Communication
from django.contrib import admin

class SubscriberAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User information',               {'fields': ['first_name', 'last_name', 'email', 'username', 'password', 'sub_type']}),
        ('custom information', {'fields': ['date_created', 'address'], 'classes': ['collapse']}),
    ]

admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Product)
admin.site.register(GetPayment)
admin.site.register(Communication)

