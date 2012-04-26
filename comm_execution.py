import os, sys, datetime
os.environ['DJANGO_SETTINGS_MODULE'] = "eeditionautomate.settings"
from datetime import timedelta
from django.core.management import setup_environ
sys.path.append('/home/anthony/')
from django.core import mail
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from eeditionautomate import settings
from signup.models import Product, SimpleSubscriber, Subscription, Communication

today = datetime.date.today()
products = Product.objects.all()
subscribers = SimpleSubscriber.objects.all()
messages = Communication.objects.all()

for object in subscribers:

    sub_startdate = object.sub_startdate
    subtype = object.sub_type.duration_type
    duration = object.sub_type.duration
    subscriber_email = object.email

    if subtype == "week":
        expires = duration * 7
    else:
        expires = duration

    sub_expires = sub_startdate + timedelta(days=expires)

    if sub_startdate == today:
        print "Thanks for signing up!"
        for object in messages:
            #if object.comm_event == 
            if object.comm_name == "Thank you for signing up":
                subject = object.comm_name
                from_email = 'nns.aroberts@gmail.com'
                to = subscriber_email
                text_content = 'text content'
                html_content = object.comm_message
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            else:
                pass
    elif sub_expires >= today:
        print "This is a current subscriber."
        for object in messages:
            if object.comm_name == "Today's Newspaper":
                subject = object.comm_name
                from_email = 'nns.aroberts@gmail.com'
                to = subscriber_email
                text_content = 'text content'
                html_content = object.comm_message
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            else:
                pass
    elif sub_expires < today:
        print "This subscription is expired."
        for object in messages:
            if object.comm_name == "Expired":
                subject = object.comm_name
                from_email = 'nns.aroberts@gmail.com'
                to = subscriber_email
                text_content = 'text content'
                html_content = object.comm_message
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            else:
                pass
    else:
        print "Something went terribly wrong"
        pass


"""
        
        send_mail()

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

