from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import Client
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from django.contrib.auth import authenticate


class MyTests(StaticLiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome(r"C:/Users/nliam/OneDrive/Documents/chromedriver_win32/chromedriver.exe")
        self.client = Client()
        self.user = User.objects.create_superuser(username='test', password='Test1234', email='test@test.com', is_active=True)
        self.user.save()

    def tearDown(self):
        self.selenium.quit()

    def test_login(self):
        self.user = authenticate(username='test', password='Test1234')
        if self.user is not None:  # prints Backend login failed
            self.user = User.objects.get(username='test')
            print(self.user.username)  # prints test
            print(self.user.password)  # prints Test1234
            self.login = self.client.login(username='test', password='Test1234')
            self.assertEqual(self.login, True)
            print("Backend login successful")

            self.selenium.get('%s%s' % (self.live_server_url, '/admin/'))
            username_input = self.selenium.find_element(by=By.NAME, value="username")
            username_input.send_keys(self.user.username)
            password_input = self.selenium.find_element(by=By.NAME, value="password")
            password_input.send_keys('Test1234')
            self.selenium.find_element(by=By.XPATH, value='//input[@value="Log in"]').click()
            time.sleep(1)

        else:
            print("Backend login failed")