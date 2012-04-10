from eeditionautomate.signup.models import Product, SimpleSubscriber, GetPayment, ProductForm, SubscriberForm
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm


def select_product(request):
    title = "get yourself an e-edition. wurd."
    pform = Product.objects.order_by('product_active')
    #pform = ProductForm(request.POST)  
    if request.method == 'POST': # If the form has been submitted...
        pform = ProductForm(request.POST) # A form bound to the POST data
        #sform = SubscriberForm(request.POST)
        if pform.is_valid(): # All validation rules pass 
            # ...
            return HttpResponseRedirect('signup/%i' % pform.id) # Redirect after POST
    else:
        form = ProductForm() # An unbound form
    return render_to_response('signup/index.html', {'title': title, 'pform': pform}, context_instance=RequestContext(request))
        

#@login_required
def subscriber_signup(request, product_id):
    signup = Product.objects.get(id=product_id)
    title = "get yourself an e-edition. wurd."  
    if request.method == 'POST': # If the form has been submitted...
        sform = SubscriberForm(request.POST) # A form bound to the POST data
        if sform.is_valid(): # All validation rules pass
            sform.sub_type = signup
            sform.save()
            return HttpResponseRedirect('signup/thankyou/') # Redirect after POST
    else:
        sform = SubscriberForm() # An unbound form
    return render_to_response('signup/detail.html', {'title': title, 'sform': sform, 'signup': signup,}, context_instance=RequestContext(request))
   

def thankyou(request):
    title = "thank you world"
    return render_to_response('signup/thankyou.html', {'title': title}, context_instance=RequestContext(request))
