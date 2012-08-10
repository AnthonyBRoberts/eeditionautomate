import datetime
from django.contrib.auth.models import User, UserManager
from django.contrib.localflavor.us.models import USStateField
from django.db import models
from django import forms
from django.forms import ModelForm
from django.forms.models import modelform_factory
from django.core.mail import send_mail
#from ckeditor.widgets import CKEditorWidget
#from ckeditor.fields import RichTextField


class Publisher(User):
    def __unicode__(self):
        return self.publisher.first_name
        #return self.get_full_name()

class PublisherUserProfile(models.Model):
    publisher = models.ForeignKey(Publisher, unique=True)
    def __unicode__(self):
        return "%s: %s" % (self.user.get_full_name(), self.publisher.first_name)


class Product(models.Model):
    publisher = models.ForeignKey(Publisher)
    product_type = models.CharField(max_length=100)
    product_description = models.CharField(max_length=255)
    product_cost = models.DecimalField(decimal_places=2, max_digits=5)
    product_active = models.BooleanField()
    duration = models.IntegerField()
    duration_type = models.CharField(max_length=32, choices=[
    ("day", "Days"),
    ("week", "Weeks")])
    @models.permalink
    def get_absolute_url(self):
        return ('subscriber_signup', (), {'publisher_id': self.publisher_id, 'product_id': self.id})
    def __unicode__(self):
        return self.product_type

class Subscription(models.Model):
    publisher = models.ForeignKey(Publisher)
    product = models.ForeignKey(Product)
    starts = models.DateField()
    def expires(self):
        from datetime import timedelta
        if self.product.duration_type == "day":
            days = self.product.duration
        elif self.product.duration_type == "week":
            days = self.product.duration * 7
        return self.starts + timedelta(days=days)

class SimpleSubscriber(User):
    publisher = models.ForeignKey(Publisher)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = USStateField()
    zipcode = models.CharField(max_length=9)
    phone = models.CharField(max_length=10)
    date_created = models.DateField(null=True)
    sub_type = models.ForeignKey(Product)
    sub_startdate = models.DateField()

    #class Meta:
        #unique_together = ("publisher", "sub_type")

    def __unicode__(self):
        return self.last_name

class FileUploader(models.Model):
    publisher = models.ForeignKey(Publisher)
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='files/%Y/%m/%d/')

    def __unicode__(self):
        return self.title



class Communication(models.Model):
    publisher = models.ForeignKey(Publisher)
    comm_name = models.CharField(max_length=50)
    comm_message = models.CharField(max_length=500)
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
        exclude = ('email', 'is_staff', 'is_active', 'is_superuser', 'date_created', 'sub_type', 'sub_startdate', 'publisher', 'groups', 'user_permissions', 'last_login', 'date_joined',)
    username = forms.EmailField(label="Email address", max_length=75)
    password = forms.CharField(label="Password", help_text="")
    def clean_email(self):
        email = self.cleaned_data['username']
        return email
