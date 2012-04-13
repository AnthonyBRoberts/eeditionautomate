from eeditionautomate.signup.models import Product, SimpleSubscriber, GetPayment, ProductForm, SubscriberForm
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
import datetime


def select_product(request):
    title = "get yourself an e-edition. wurd."
    pform = Product.objects.order_by('product_active')  
    if request.method == 'POST': # If the form has been submitted...
        pform = ProductForm(request.POST) # A form bound to the POST data
        if pform.is_valid(): # All validation rules pass 
            # ...
            return HttpResponseRedirect('signup/%i' % pform.id) # Redirect after POST
    else:
        form = ProductForm() # An unbound form
    return render_to_response('signup/index.html', {'title': title, 'pform': pform}, context_instance=RequestContext(request))
        

def subscriber_signup(request, product_id):
    productchoice = Product.objects.get(id=product_id)
    now = datetime.datetime.now()
    title = "We need some information."  
    if request.method == 'POST': # If the form has been submitted...
        sform = SubscriberForm(request.POST) # A form bound to the POST data
        if sform.is_valid(): # All validation rules pass
            suscriber = sform.save(commit=False)
            suscriber.date_created = now
            suscriber.sub_type = productchoice
            suscriber.save()
            return HttpResponseRedirect('thankyou/') # Redirect after POST
    else:
        sform = SubscriberForm() # An unbound form
    return render_to_response('signup/detail.html', {'title': title, 'sform': sform, 'productchoice': productchoice, 'now': now.date(),}, context_instance=RequestContext(request))
   

def thankyou(request, product_id):
    title = "thank you world"
    return render_to_response('signup/thankyou.html', {'title': title}, context_instance=RequestContext(request))
