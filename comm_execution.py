#from django.conf import settings
import os, sys, datetime
# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "eeditionautomate.settings"
from datetime import timedelta
from django.core.management import setup_environ
sys.path.append('/home/anthony/')
from eeditionautomate import settings
from django.core.mail import send_mail
from signup.models import Product, SimpleSubscriber, Subscription



today = datetime.datetime.today()

products = Product.objects.all()
subscribers = SimpleSubscriber.objects.all()

for object in subscribers:
    sub_startdate = object.sub_startdate
    subtype = object.sub_type.duration_type
    duration = object.sub_type.duration
    if subtype == "week":
        expires = duration * 7
    else:
        expires = duration

    sub_expires = sub_startdate + timedelta(expires)
    if sub_expires < today:
        print "Expired, you mutha-fucka!"
    elif sub_expires > today:
        print "Current. Oh Long Johnson!"
    else:
        print "Something went terribly wrong"


"""
if Product.duration_type == "week":
messages = Communication.objects.all()

#for object in messages:
if sub_expires > today:
    print "Still good"
    #if messages.comm_schedule == "something":
        #message = "Thing!"
        #sender = "nns.aroberts@gmail.com"
        #recipients = "recipient@gmail.com"
        #send_mail(subject, message, sender, recipients)
elif sub_expires < today: 
    print "EXPIRED! PAY MY BITCH ASS"
else:
    print "Something went terribly wrong"


stuff = Product.objects.all()

for object in stuff:
    if object.thing = True:
        subject = "Stuff!"
        message = "Thing!"
        sender = "nns.aroberts@gmail.com"
        recipients = "recipient@gmail.com"
        send_mail(subject, message, sender, recipients)
    else:
        pass
"""

