from eeditionautomate.signup.models import Product, Subscriber, GetPayment
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def select_product(request):
    title = "E-editions for Sale"
    signup_form = Product.objects.order_by('product_active')
    
#   p = get_object_or_404(Product, pk=product_id)
#    try:
#        selected_choice = p.choice_set.get(pk=request.POST['product'])
#    except (KeyError, Product.DoesNotExist):
#        # Redisplay the poll voting form.
#        return render_to_response('signup/index.html', {
#            'poll': p,
#            'error_message': "You didn't select a choice.",
#        }, context_instance=RequestContext(request))
#    else:
#        selected_choice.votes += 1
#        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
#        return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))
    return render_to_response('signup/index.html', {'signup_form': signup_form, 'title': title},
context_instance=RequestContext(request))

def subscriber_signup(request, product_id):
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
