from django import forms
from signup.models import SimpleSubscriber, Product, Publisher

class SelectProductForm(forms.Form):
    publisher = Publisher.objects.get(pk=publisher_id)
    product = Products.objects.order_by('-duration').exclude(product_active=False)#.filter(publisher=request.user)

class SubscriberInfoForm(forms.Form):
    productchoice = Product.objects.get(id=product_id)
    now = datetime.date.today()
    title = "We need some information."  
    if request.method == 'POST': # If the form has been submitted...
        sform = SubscriberForm(request.POST) # A form bound to the POST data
        if sform.is_valid(): # All validation rules pass
            subscriber = sform.save(commit=False)
            subscriber.date_created = now
            subscriber.sub_type = productchoice
            subscriber.sub_startdate = now
            subscriber.publisher = request.user
            subscriber.save()
