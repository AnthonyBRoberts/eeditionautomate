from django.test import TestCase
from signup.models import Product, Publisher
from django.contrib.auth.models import User
"""
class ProductModelTest(TestCase):
    def test_creating_new_products_and_saving_to_db(self):

        #create a new product with all attributes set


        product = Product()
        user = publisher.objects.get(id=user_id)
        product.publisher.user = user
        product.product_type = "1 year"
        product.product_description = "52 weeks"
        product.product_cost = "52.00"
        product.product_active = 1
        product.duration = 52
        product.duration_type = "week"

        #check we can save to the DB
        product.save()

        #check we can find it in the DB
        all_products_in_db = Product.objects.all()
        self.assertEquals(len(all_products_in_db), 12)
        most_recent_product_added = all_products_in_db[0]
        self.assertEquals(most_recent_product_added, product)
        
        #check that it saved attributes
        self.assertEquals(most_recent_product_added.product_type, "1 year")
"""

