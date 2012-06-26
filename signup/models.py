from django.contrib.auth.models import User, UserManager
from django.db import models
import datetime
from django import forms
from django.forms import ModelForm
from django.core.mail import send_mail
from ckeditor.widgets import CKEditor
from ckeditor.fields import HTMLField


class Publisher(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField()
    start_date = models.DateField()
    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    publisher = models.ForeignKey(Publisher)
    def __unicode__(self):
        return "%s: %s" % (self.user.get_full_name(), self.publisher.name)


class Product(models.Model):
    publisher = models.ForeignKey(User)
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
    publisher = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    starts = models.DateField()
    def expires(self):
        from datetime import timedelta
        if self.product.duration_type == "day":
            days = self.product.duration
        elif self.product.duration_type == "week":
            days = self.product.duration * 7
        return self.starts + timedelta(days=days)

class SimpleSubscriber(models.Model):
    publisher = models.ForeignKey(User)
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
    
    #def was_published_today(self):
        #return self.date_created.date() == datetime.date.today()

class Communication(models.Model):
    publisher = models.ForeignKey(User)
    comm_name = models.CharField(max_length=50)
    comm_message = HTMLField()
    comm_active = models.BooleanField()
    send_now = models.BooleanField()
    #class Admin:
        # various admin options are here
        #list_display  = ('comm_name', 'comm_active'),
        #search_fields = ['comm_name',],
        #js = ('/tiny_mce/tiny_mce.js', '/appmedia/admin/js/textareas.js',),
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
    days = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label="")
    days = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
    SUBSCRIBER_GROUPS = (
    ('0', 'Active'),
    ('1', 'Lapsed'),
    ('2', 'All'),
)
    sub_status = models.CharField(max_length=1, choices=SUBSCRIBER_GROUPS)
    def save(self, *args, **kwargs):
        super(Communication, self).save(*args, **kwargs) #Call the "real" save() method.
        if self.send_now == True:
            subscribers = SimpleSubscriber.objects.all()
            messages = Communication.objects.all()
            for object in subscribers:
                subscriber_email = object.email
            for object in messages:
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

class ProductForm(ModelForm):
    publisher = models.ForeignKey(Publisher)
    class Meta:
        model = Product
        fields = ('product_type',)

class SubscriberForm(ModelForm):
    publisher = models.ForeignKey(Publisher)
    class Meta:
        model = SimpleSubscriber
        exclude = ('date_created', 'sub_type', 'sub_startdate')
"""
class Publisher(User):   
    def was_published_today(self):
        return self.date_created.date() == datetime.date.today()

class GetPayment(models.Model):
    payment_made = models.BooleanField()
    payment_amount = models.DecimalField(decimal_places=2, max_digits=4)
    payment_date = models.DateTimeField('payment date')
    # payment_type = models.ForeignKey(product_name)
"""
