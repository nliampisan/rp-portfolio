# from django.test import TestCase

# Create your tests here.
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

# class PythonOrgSearch(unittest.TestCase,StaticLiveServerTestCase):
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r"C:/Users/nliam/OneDrive/Documents/chromedriver_win32/chromedriver.exe")

    # def test_search_in_python_org(self):
    #     driver = self.driver
    #     driver.get("http://www.python.org")
    #     self.assertIn("Python", driver.title)

    def test_search_in_project(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/projects/")
        self.assertIn("Projects", driver.page_source)


    def tearDown(self):
        self.driver.close()
