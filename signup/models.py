from django.contrib.auth.models import User, UserManager
from django.db import models
import datetime
from django import forms
from django.forms import ModelForm


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

#

class SimpleSubscriber(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=9)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    date_created = models.DateField(null=True)
    sub_type = models.ForeignKey(Product)
    sub_startdate = models.DateField()
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
    send_now = models.BooleanField()
    comm_schedule = models.DateTimeField('communication schedule')
    DAYS_OF_WEEK = (
    ('0', 'Monday'),
    ('1', 'Tuesday'),
    ('2', 'Wednesday'),
    ('3', 'Thursday'),
    ('4', 'Friday'),
    ('5', 'Saturday'),
    ('6', 'Sunday'),
)
    #days = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label="")
    days = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
    SUBSCRIBER_GROUPS = (
    ('0', 'Active'),
    ('1', 'Lapsed'),
    ('2', 'All'),
)
    #sub_status = models.CharField(max_length=1, choices=SUBSCRIBER_GROUPS)
    def save(self, *args, **kwargs):
        super(Communication, self).save(*args, **kwargs) #Call the "real" save() method.
        if self.send_now == True:
            subscribers = SimpleSubscriber.objects.all()
            messages = Communication.objects.all()
            for object in subscribers:
                subscriber_email = object.email
            for object in 
            #if self.SUBSCRIBER_GROUPS == "Active":
                subject = object.comm_name
                message = object.comm_message
                sender = "nns.aroberts@gmail.com"
                recipients = subscriber_email
                send_mail(subject, message, sender, [recipients], fail_silently=False)
            else:
                pass
    def __unicode__(self):
        return self.comm_name    

    
class Subscriber(User):
    address = models.CharField(max_length=200)
    date_created = models.DateField('created date')
    sub_type = models.ForeignKey(Product)
    #def __unicode__(self):
    #def get_absolute_url(self):
      #  return "/signup/%s/%s/" % (self.date_created, 
    #    return self.user_ptr_id    
    def was_published_today(self):
        return self.date_created.date() == datetime.date.today()

