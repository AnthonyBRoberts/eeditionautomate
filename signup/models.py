from django.contrib.auth.models import User, UserManager
from django.db import models
import datetime
from django import forms
from django.forms import ModelForm

#class SignupForm(forms.Form):
#    subject = forms.CharField(max_length=100)
#    message = forms.CharField()
#    sender = forms.EmailField()
#    cc_myself = forms.BooleanField(required=False)

class Product(models.Model):
    product_type = models.CharField(max_length=100)
    product_description = models.CharField(max_length=255)
    product_cost = models.DecimalField(decimal_places=2, max_digits=5)
    product_active = models.BooleanField()
    duration = models.IntegerField()
    duration_type = models.CharField(max_length=32, choices=[
    ("day", "Days"),
    ("week", "Weeks")])
    def get_absolute_url(self):
        return "/signup/%i/" % self.id
    def __unicode__(self):
        return self.product_type

class Subscription(models.Model):
    product = models.ForeignKey(Product)
    starts = models.DateField()
    def expires(self):
        from datetime import timedelta
        if self.product.duration_type == "day":
            days = self.product.duration
        elif self.product.duration_type == "week":
            days = self.product.duration * 7
        return self.starts + timedelta(days=days)


class Subscriber(User):
    address = models.CharField(max_length=200)
    date_created = models.DateTimeField('created date')
    sub_type = models.ForeignKey(Product)
    #def __unicode__(self):
    #def get_absolute_url(self):
      #  return "/signup/%s/%s/" % (self.date_created, 
    #    return self.user_ptr_id    
    def was_published_today(self):
        return self.date_created.date() == datetime.date.today()

class SimpleSubscriber(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=9)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    date_created = models.DateTimeField(null=True)
    sub_type = models.ForeignKey(Product)
    sub_startdate = models.DateTimeField()
    def __unicode__(self):
        return self.name
    #def get_absolute_url(self):
        #return "/signup/%s/%s/" % (self.date_created, self.user_ptr_id)    
    #def was_published_today(self):
    #    return self.date_created.date() == datetime.date.today()

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('product_type',)

class SubscriberForm(ModelForm):
    class Meta:
        model = SimpleSubscriber
        exclude = ('date_created', 'sub_type', 'sub_startdate')

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
    """
    DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)
    days = models.CharField(max_length=1, choices=DAYS_OF_WEEK
    """
    def __unicode__(self):
        return self.comm_name
