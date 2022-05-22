import numpy as np
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from GP.testcasegen import TestCaseGenerator
from GP.function import *
import random
import string

primitives = ["link", "button", "input-text", "text-area"]


class Evaluator:
    def __init__(self):
        pass

    def eval_pop(self, pop):
        for indiv in pop.indivs:
            self.eval_indiv(indiv)

    def eval_indiv(self, indiv):
        self.driver = webdriver.Chrome(r"C:/Users/nliam/OneDrive/Documents/chromedriver_win32/chromedriver.exe")
        self.driver.get('http://127.0.0.1:8000/projects/')
        cur_url = 'http://127.0.0.1:8000/projects/'
        num_success_actions = 0
        num_webpages = 0
        for gene in indiv.genes:
            element_type = gene.get_type()
            new_url = self.driver.current_url
            gene.set_url(new_url)
            if element_type == 0:
                elems = self.driver.find_elements(by=By.XPATH, value="//a[@href]")
                elem_offset = random.randint(0,len(elems)-1)
                try:
                    elems[elem_offset].click()
                except:
                    continue
                num_success_actions += 1
                if self.driver.current_url != cur_url:
                    num_webpages += 1
                    cur_url = self.driver.current_url
            elif element_type == 1:
                elems = self.driver.find_elements(by=By.TAG_NAME, value="button")
                elem_offset = random.randint(0,len(elems)-1)
                try:
                    elems[elem_offset].click()
                except:
                    continue
                num_success_actions += 1
                if self.driver.current_url != cur_url:
                    num_webpages += 1
                    cur_url = self.driver.current_url

            elif element_type == 2:
                elems = self.driver.find_elements(by=By.XPATH, value="//input[@type='text']")
                input_data = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(1,10)))
                # print(input_data)
                try:
                    elem_offset = random.randint(0, len(elems) - 1)
                    # print(elems[elem_offset].get_attribute("name"))
                    # print(input_data)
                    elems[elem_offset].send_keys(input_data)
                    # print("send key success")
                except:
                    continue
                num_success_actions += 1
                if self.driver.current_url != cur_url:
                    num_webpages += 1
                    cur_url = self.driver.current_url

            elif element_type == 3:
                elems = self.driver.find_elements(by=By.TAG_NAME, value="textarea")
                input_data = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(1,10)))
                # print(input_data)
                try:
                    elem_offset = random.randint(0, len(elems) - 1)
                    # print(elems[elem_offset].get_attribute("name"))
                    # print(input_data)
                    elems[elem_offset].send_keys(input_data)
                    # print("send key success")
                except:
                    continue
                num_success_actions += 1
                if self.driver.current_url != cur_url:
                    num_webpages += 1
                    cur_url = self.driver.current_url
            else:
                pass
        indiv.fitness = num_success_actions + 10*num_webpages
        self.driver.close()