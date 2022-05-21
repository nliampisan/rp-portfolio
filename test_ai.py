from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import Client
from selenium.webdriver.common.by import By
from selenium import webdriver
from blog.models import *
from projects.models import *
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver import ActionChains
# https://www.geeksforgeeks.org/action-chains-in-selenium-python/
import time
import datetime
from django.contrib.auth import authenticate

class MyTests(StaticLiveServerTestCase):

    def setUp(self):
        self.patient = User.objects.create_user(first_name="first", last_name="last",
                                                email='patient@example.com', password="password",
                                                username='patient@example.com')
        self.patient.save()

        self.project = Project.objects.create(title="Project1", description="first project", technology="Java", image="")
        self.project.save()
        self.cat = Category.objects.create(name="Category 1")
        self.cat.save()
        self.post = Post.objects.create(title="Post A", body="Post Body")
        self.post.save()
        self.post.categories.add(self.cat)
        self.comment = Comment.objects.create(author="Author", body="Comment Body", post=self.post)
        self.comment.save()


        self.driver = webdriver.Chrome(r"C:/Users/nliam/OneDrive/Documents/chromedriver_win32/chromedriver.exe")
        self.client = Client()
        self.driver.get('%s%s' % (self.live_server_url, '/projects/'))
        # link =  self.driver.find_element(by=By.CLASS_NAME, value='navbar-brand');
        # link.click()
        print("all links")
        all_links = self.driver.find_elements(by=By.TAG_NAME, value="a")
        for link in all_links:
            print(link.get_attribute("href"))

        print("all inputs")
        all_inputs = self.driver.find_elements(by=By.TAG_NAME, value="input")
        for input in all_inputs:
            print(str(input.get_attribute("name"))+" "+str(input.get_attribute("type")))


        print("xpath ahref")
        elems = self.driver.find_elements(by=By.XPATH,value="//a[@href]")
        for elem in elems:
            print(elem.get_attribute("href"))

        print("all btns")
        btn = self.driver.find_element(by=By.CLASS_NAME, value="btn")
        print(btn.get_attribute("href"))
        btn.click()

        print()
        print("blogs")
        self.driver.get('%s%s' % (self.live_server_url, '/blog/'))
        all_links = self.driver.find_elements(by=By.TAG_NAME, value="a")
        for link in all_links:
            print(link.get_attribute("href"))

        print()
        print("blog form:")
        self.driver.get('%s%s' % (self.live_server_url, '/blog/1/'))

        self.driver.implicitly_wait(5)

        print("all inputs:")
        all_inputs = self.driver.find_elements(by=By.TAG_NAME, value="input")
        for input in all_inputs:
            print(str(input.get_attribute("name")) + " " + str(input.get_attribute("type")))

        print("xpath text:")
        elems = self.driver.find_elements(by=By.XPATH, value="//input[@type='text']")
        for elem in elems:
            print(elem.get_attribute("name"))
            elem.send_keys("author")
        # time.sleep(5)
        print("all btns:")
        try:
            btn = self.driver.find_element(by=By.CLASS_NAME, value="btn")
            print(btn.get_attribute("name"))
            print("found")
            btn.click()
            # time.sleep(2)
            print("after sleep")
        except:
            print("not found")

        print("contents")
        try:
            contents = self.driver.find_elements(by=By.TAG_NAME, value="form")
            for content in contents:
                print(content.get_attribute("name"))
                print("found")
        except:
            print("not found")


        print("button tag")
        all_buttons = self.driver.find_elements(by=By.TAG_NAME, value="button")
        for button in all_buttons:
            print(str(button.get_attribute("name")) + " " + str(button.get_attribute("type")))
        # input.click()
        # time.sleep(5)
        WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(5)

        print("text area")
        all_inputs = self.driver.find_elements(by=By.TAG_NAME, value="textarea")
        for input in all_inputs:
            print(str(input.get_attribute("name")) + " " + str(input.get_attribute("type")))
        input.send_keys("text area")
        time.sleep(2)
        button.click()
        time.sleep(10)
    def tearDown(self):
        self.driver.close()

    def test_something(self):
        self.assertEqual(True, True)
