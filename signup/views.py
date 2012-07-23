from eeditionautomate.signup.models import Publisher, Product, SimpleSubscriber, ProductForm, SubscriberForm, User
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.formtools.preview import FormPreview
from django.forms import ModelForm
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import datetime


def select_product(request, publisher_id):
    #p = get_object_or_404(Product, pk=product)
    publisher = Publisher.objects.get(id=publisher_id)
    title = "Please select your subscription"
    pform = Product.objects.order_by('-duration').exclude(product_active=False).filter(publisher=publisher_id)
    """
    try:
        selected_product = p.choice_set.get(pk=request.POST['product'])
    except (KeyError, Choice.DoesNotExist):
        return render_to_response('signup/
"""
    if request.method == 'POST': # If the form has been submitted...
        pform = ProductForm(request.POST) # A form bound to the POST data
        if pform.is_valid(): # All validation rules pass 
            url = reverse('subscriber_signup', args={'product_id': product_id, 'publisher_id': publisher_id})
            return HttpResponseRedirect(url) # Redirect after POST
    else:
        form = ProductForm() # An unbound form
    return render_to_response('signup/index.html', {'publisher': publisher, 'title': title, 'pform': pform,}, context_instance=RequestContext(request, publisher_id))

        

def subscriber_signup(request, publisher_id, product_id):
    publisher = Publisher.objects.get(id=publisher_id)
    productchoice = Product.objects.get(id=product_id)
    now = datetime.date.today()
    title = "We need some information."  
    if request.method == 'POST': # If the form has been submitted...
        sform = SubscriberForm(request.POST) # A form bound to the POST data
        if sform.is_valid(): # All validation rules pass
            subscriber = sform.save(commit=False)
            #subscriber.username = email
            subscriber.date_created = now
            subscriber.sub_type = productchoice
            subscriber.sub_startdate = now
            subscriber.publisher = Publisher.objects.get(id=publisher_id)
            subscriber.save()
            return HttpResponseRedirect('/signup/%s/%s/paypal/' % (publisher_id, product_id)) # Redirect after POST
    else:
        sform = SubscriberForm() # An unbound form
    return render_to_response('signup/detail.html', {'publisher': publisher, 'title': title, 'sform': sform, 'productchoice': productchoice, 'now': now,}, context_instance=RequestContext(request))
   

#def thankyou(request, product_id):
#    title = "thank you world"
#    return render_to_response('/paypal', {'title': title}, context_instance=RequestContext(request))

def paypal(request, publisher_id, product_id):

# What you want the button to do.
    productchoice = Product.objects.get(id=product_id)
    publisher = Publisher.objects.get(id=publisher_id)
    paypal_dict = {
"business": settings.PAYPAL_RECEIVER_EMAIL,
"amount": "%.2f" % productchoice.product_cost,
"item_name": "%s" % productchoice.product_type,
"invoice": "unique-invoice-id",
"notify_url": "%s%s" % (settings.SITE_NAME, reverse('paypal-ipn')),
"return_url": "http://www.example.com/your-return-location/",
"cancel_return": "http://www.example.com/your-cancel-location/",
}
# Create the instance.
    
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form.sandbox(), "productchoice": productchoice}
    return render_to_response("signup/paypal.html", context)


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

