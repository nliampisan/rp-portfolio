from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
# https://www.geeksforgeeks.org/action-chains-in-selenium-python/
import time
import datetime

class Generator:

    def gen(self):
        test_arr = []

        self.driver = webdriver.Chrome(r"C:/Users/nliam/OneDrive/Documents/chromedriver_win32/chromedriver.exe")
        self.driver.get('http://127.0.0.1:8000/projects/')

        print("xpath ahref")
        elems = self.driver.find_elements(by=By.XPATH,value="//a[@href]")
        for elem in elems:
            print(elem.location)
            test_arr.append(elem)

        # print("all inputs:")
        # all_inputs = self.driver.find_elements(by=By.TAG_NAME, value="input")
        # for input in all_inputs:
        #     print(str(input.get_attribute("name")) + " " + str(input.get_attribute("type")))
        #
        # print("xpath text:")
        # elems = self.driver.find_elements(by=By.XPATH, value="//input[@type='text']")
        # for elem in elems:
        #     print(elem.get_attribute("name"))
        #     elem.send_keys("author")
        #
        # print("all btns:")
        # try:
        #     btn = self.driver.find_element(by=By.CLASS_NAME, value="btn")
        #     print(btn.get_attribute("name"))
        #     print("found")
        # except:
        #     print("not found")
        #
        # print("button tag")
        # all_buttons = self.driver.find_elements(by=By.TAG_NAME, value="button")
        # for button in all_buttons:
        #     print(str(button.get_attribute("name")) + " " + str(button.get_attribute("type")))
        #
        # print("text area")
        # all_inputs = self.driver.find_elements(by=By.TAG_NAME, value="textarea")
        # for input in all_inputs:
        #     print(str(input.get_attribute("name")) + " " + str(input.get_attribute("type")))
        # input.send_keys("text area")
        # button.click()
        self.driver.close()
        return test_arr
