from GP.webgen import Generator
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
# https://www.geeksforgeeks.org/action-chains-in-selenium-python/
import time
import datetime

from test_ai import MyTests

myGen = Generator()

arr = myGen.gen()

# driver = webdriver.Chrome(r"C:/Users/nliam/OneDrive/Documents/chromedriver_win32/chromedriver.exe")
# driver.get('http://127.0.0.1:8000/projects/')
#
# arr[2].click()

testgen = MyTests()

arr = MyTests().setUp()

print(arr)

