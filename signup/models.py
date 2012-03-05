from django.contrib.auth.models import User, UserManager
from django.db import models
import datetime

class Product(models.Model):
    product_type = models.CharField(max_length=100)
    product_description = models.CharField(max_length=255)
    product_cost = models.DecimalField(decimal_places=2, max_digits=4)
    product_active = models.BooleanField()
    def __unicode__(self):
        return self.product_type

class Subscriber(User):
    address = models.CharField(max_length=200)
    date_created = models.DateTimeField('created date')
    sub_type = models.ForeignKey(Product)
    #def __unicode__(self):
    #    return self.user_ptr_id    
    def was_published_today(self):
        return self.date_created.date() == datetime.date.today()

class GetPayment(models.Model):
    payment_made = models.BooleanField()
    payment_amount = models.DecimalField(decimal_places=2, max_digits=4)
    payment_date = models.DateTimeField('payment date')
    # payment_type = models.ForeignKey(product_name)

class Communication(models.Model):
    comm_name = models.CharField(max_length=50)
    comm_message = models.CharField(max_length=255)
    comm_active = models.BooleanField()
    comm_schedule = models.DateTimeField('communication schedule')
    def __unicode__(self):
        return self.comm_name
