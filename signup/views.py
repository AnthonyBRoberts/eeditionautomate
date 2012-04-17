from eeditionautomate.signup.models import Product, SimpleSubscriber, GetPayment, ProductForm, SubscriberForm
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import datetime


def select_product(request):
    title = "Please select your subscription"
    pform = Product.objects.order_by('product_type').exclude(product_active=False)
    if request.method == 'POST': # If the form has been submitted...
        pform = ProductForm(request.POST) # A form bound to the POST data
        if pform.is_valid(): # All validation rules pass 
            # ...
            return HttpResponseRedirect('signup/%i' % pform.id) # Redirect after POST
    else:
        form = ProductForm() # An unbound form
    return render_to_response('signup/index.html', {'title': title, 'pform': pform}, context_instance=RequestContext(request))
    return 
        

def subscriber_signup(request, product_id):
    productchoice = Product.objects.get(id=product_id)
    now = datetime.datetime.now()
    title = "We need some information."  
    if request.method == 'POST': # If the form has been submitted...
        sform = SubscriberForm(request.POST) # A form bound to the POST data
        if sform.is_valid(): # All validation rules pass
            subscriber = sform.save(commit=False)
            subscriber.date_created = now
            subscriber.sub_type = productchoice
            subscriber.save()
            return HttpResponseRedirect('/paypal') # Redirect after POST
    else:
        sform = SubscriberForm() # An unbound form
    return render_to_response('signup/detail.html', {'title': title, 'sform': sform, 'productchoice': productchoice, 'now': now.date(),}, context_instance=RequestContext(request))
   

def thankyou(request, product_id):
    title = "thank you world"
    return render_to_response('/paypal', {'title': title}, context_instance=RequestContext(request))

def paypal(request):
# What you want the button to do.
    paypal_dict = {
"business": settings.PAYPAL_RECEIVER_EMAIL,
"amount": "1.00",
"item_name": "name of the item",
"invoice": "unique-invoice-id",
"notify_url": "%s%s" % (settings.SITE_NAME, reverse('paypal-ipn')),
"return_url": "http://www.example.com/your-return-location/",
"cancel_return": "http://www.example.com/your-cancel-location/",
}
# Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form.sandbox()}
    return render_to_response("signup/paypal.html", context)
# paypal.html

"""
@require_POST
@csrf_exempt
def ipn(request, item_check_callable=None):
  
    PayPal IPN endpoint (notify_url).
    Used by both PayPal Payments Pro and Payments Standard to confirm transactions.
    http://tinyurl.com/d9vu9d
    PayPal IPN Simulator:
    https://developer.paypal.com/cgi-bin/devscr?cmd=_ipn-link-session
    
    flag = None
    ipn_obj = None
    form = PayPalIPNForm(request.POST)
    if form.is_valid():
        try:
            ipn_obj = form.save(commit=False)
        except Exception, e:
            flag = "Exception while processing. (%s)" % e
    else:
        flag = "Invalid form. (%s)" % form.errors

    if ipn_obj is None:
        ipn_obj = PayPalIPN()

    ipn_obj.initialize(request)

    if flag is not None:
        ipn_obj.set_flag(flag)
    else:
        # Secrets should only be used over SSL.
        if request.is_secure() and 'secret' in request.GET:
            ipn_obj.verify_secret(form, request.GET['secret'])
        else:
            try:
                ipn_obj.verify(item_check_callable)
            except Exception, e:
                flag = "Exception while processing. (%s)" % e
    ipn_obj.save()

    return HttpResponse("OKAY") 
"""

