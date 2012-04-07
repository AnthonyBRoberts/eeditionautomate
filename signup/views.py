from eeditionautomate.signup.models import Product, Subscriber, GetPayment, ProductForm, SubscriberForm
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm


def select_product(request):
    title = "get yourself an e-edition. wurd."
    #form = ProductForm(request.POST)  
    if request.method == 'POST': # If the form has been submitted...
        form = SubscriberForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('signup/thankyou.html') # Redirect after POST
    else:
        form = SubscriberForm() # An unbound form
    return render_to_response('signup/index.html', {'title': title, 'form': form}, context_instance=RequestContext(request))
        

@login_required
def subscriber_signup(request, product_id):
    signup = Product.objects.get(id=product_id)
    return render_to_response('signup/thankyou.html', {
        'product': signup,
    })
    #title = "this is a title"
    #subscriber_signup_form = Subscriber.sub_type
    #p = get_object_or_404(Product, product_id)
    #try:
     #   selected_choice = p.product_type.get(product_id=request.POST['product'])
    #except (KeyError, Product.DoesNotExist):
        # Redisplay the poll voting form.
        #return render_to_response('signup/index.html', {
         #   'product': p,
          #  'error_message': "You didn't select a choice.",
       # }, context_instance=RequestContext(request))
   # else:
     #   selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
      #  return HttpResponseRedirect(reverse('signup_result', args=(p.id,)))
