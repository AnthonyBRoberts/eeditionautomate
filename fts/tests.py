"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.utils import unittest
from django.test import TestCase
from django.test.client import Client
from django_liveserver.testcases import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys


class EEAutomateTest(LiveServerTestCase):
    fixtures = ['admin_user.json']

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(EEAutomateTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(EEAutomateTest, cls).tearDownClass()
        cls.selenium.quit()

    def test_can_create_new_product_via_admin_site(self):

        #Bob opens the browser, goes to admin page
        self.selenium.get(self.live_server_url + '/admin/')

        #Does Bob see the page title?
        body = self.selenium.find_element_by_tag_name('body')
        self.assertIn('E-Edition Automation Administration', body.text)

        #Bob types username & password and hits return
        username_field = self.selenium.find_element_by_name('username')
        username_field.send_keys('anthony')
        password_field = self.selenium.find_element_by_name('password')
        password_field.send_keys('M@ximus01')
        password_field.send_keys(Keys.RETURN)

        #Bob's login successful, goes to admin home page
        body = self.selenium.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)

        #Bob sees products link
        products_link = self.selenium.find_elements_by_link_text('Products')
        self.assertEquals(len(products_link), 1)

        #TODO: Finish this test
        self.fail('finish this test')
