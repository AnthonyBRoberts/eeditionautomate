from eeditionautomate.signup.models import Product
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    title = "Why doesn't the fucking signup_form render?"
    signup_form = Product.objects.order_by('product_active')
    return render_to_response('signup/index.html', {'signup_form': signup_form, 'title': title},
context_instance=RequestContext(request))
#def index(request):
#    title = "this is a title"
#    signup_form = Product.objects.order_by("product_active")
#    return render_to_response('index.html', {
 #       'signup_form': signup_form,
  #      'title': title,
   # })

#def index(request):
#    return HttpResponse("You're looking at index")

#def results(request, poll_id):
#    return HttpResponse("You're looking at the results of poll %s." % poll_id)

#def vote(request, poll_id):
#    return HttpResponse("You're voting on poll %s." % poll_id)
