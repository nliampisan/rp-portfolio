from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import Client
from selenium.webdriver.common.by import By
from selenium import webdriver
from blog.models import *
from projects.models import *
from selenium.webdriver.support.ui import WebDriverWait
import random

from selenium.webdriver import ActionChains
# https://www.geeksforgeeks.org/action-chains-in-selenium-python/
import time
import datetime
import string
from django.contrib.auth import authenticate

class MyTests(StaticLiveServerTestCase):

    def setUp(self):
        self.new_user = User.objects.create_user(first_name="first", last_name="last",
                                                email='patient@example.com', password="password",
                                                username='patient@example.com')
        self.new_user.save()
        self.project = Project.objects.create(title="Project1", description="first project", technology="Java", image="")
        self.project.save()
        self.project2 = Project.objects.create(title="Project2", description="second project", technology="Java",image="")
        self.project2.save()
        self.cat = Category.objects.create(name="Category 1")
        self.cat.save()
        self.cat2 = Category.objects.create(name="Category 2")
        self.cat2.save()
        self.post = Post.objects.create(title="Post A", body="Post Body")
        self.post.save()
        self.post.categories.add(self.cat)
        self.post2 = Post.objects.create(title="Post B", body="Post Body")
        self.post2.save()
        self.post2.categories.add(self.cat2)
        self.comment = Comment.objects.create(author="Author", body="Comment Body", post=self.post)
        self.comment.save()

        self.driver = webdriver.Chrome(r"C:/Users/nliam/OneDrive/Documents/chromedriver_win32/chromedriver.exe")
        self.client = Client()
        self.driver.get('%s%s' % (self.live_server_url, '/projects/'))

        # testcase = [1,0,2,0,3,3,3,3,1,0]
        testcase = [0,0,0,0,0,0,2,0,0,1]
        for gene in testcase:
            element_type = gene
            if element_type == 0:
                elems = self.driver.find_elements(by=By.XPATH, value="//a[@href]")
                elem_offset = random.randint(0,len(elems)-1)
                try:
                    elems[elem_offset].click()
                    print("success")
                except:
                    continue

            elif element_type == 1:
                elems = self.driver.find_elements(by=By.TAG_NAME, value="button")
                elem_offset = random.randint(0,len(elems)-1)
                try:
                    elems[elem_offset].click()
                    print("success")

                except:
                    continue


            elif element_type == 2:
                elems = self.driver.find_elements(by=By.XPATH, value="//input[@type='text']")
                input_data = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(1,10)))
                # print(input_data)
                try:
                    elem_offset = random.randint(0, len(elems) - 1)
                    # print(elems[elem_offset].get_attribute("name"))
                    # print(input_data)
                    elems[elem_offset].send_keys(input_data)
                    print("send key success")
                except:
                    continue

            elif element_type == 3:
                elems = self.driver.find_elements(by=By.TAG_NAME, value="textarea")
                input_data = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(1,10)))
                # print(input_data)
                try:
                    elem_offset = random.randint(0, len(elems) - 1)
                    # print(elems[elem_offset].get_attribute("name"))
                    # print(input_data)
                    elems[elem_offset].send_keys(input_data)
                    print("send key success")
                except:
                    continue
            else:
                pass

    def tearDown(self):
        self.driver.close()

    def test_something(self):
        self.assertEqual(True, True)
