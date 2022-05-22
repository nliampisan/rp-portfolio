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
    def __init__(self, primitives, test_cases, num_regs):
        # self.params = params
        self.num_regs = num_regs
        self.registers = np.zeros(self.num_regs)
        self.primitives = primitives
        self.num_primitives = len(primitives)
        self.test_cases = test_cases

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
            gene.set_url(self.driver.current_url)
            if element_type == 0:
                try:
                    elems = self.driver.find_elements(by=By.XPATH, value="//a[@href]")
                    try:
                        elems[random.randint(len(elems))].click()
                        num_success_actions += 1
                        if self.driver.current_url != cur_url:
                            num_webpages += 1
                            cur_url = self.driver.current_url
                    except:
                        pass
                except:
                    pass
            elif element_type == 1:
                try:
                    elems = self.driver.find_elements(by=By.TAG_NAME, value="button")
                    try:
                        elems[random.randint(len(elems))].click()
                        num_success_actions += 1
                        if self.driver.current_url != cur_url:
                            num_webpages += 1
                            cur_url = self.driver.current_url
                    except:
                        pass
                except:
                    pass
            elif element_type == 2:
                try:
                    elems = self.driver.find_elements(by=By.XPATH, value="//input[@type='text']")
                    try:
                        input_data = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(10)))
                        elems[random.randint(len(elems))].send_keys(input_data)
                        num_success_actions += 1
                        if self.driver.current_url != cur_url:
                            num_webpages += 1
                            cur_url = self.driver.current_url
                    except:
                        pass
                except:
                    pass

            elif element_type == 3:
                try:
                    elems = self.driver.find_elements(by=By.TAG_NAME, value="textarea")
                    try:
                        input_data = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(10)))
                        elems[random.randint(len(elems))].send_keys(input_data)
                        num_success_actions += 1
                        if self.driver.current_url != cur_url:
                            num_webpages += 1
                            cur_url = self.driver.current_url
                    except:
                        pass
                except:
                    pass
            else:
                pass
            # indiv.fitness = float(-sum_sq_err / len(test_cases))
        indiv.fitness = num_success_actions + 10*num_webpages

    def decode_indiv(self, indiv):
        program = ""
        for instr in indiv.genes:
            opcode, out, in1, in2 = self._decode_instr(instr)
            line = (primitives[opcode][1] + "\n")
            line = line.replace("out", str(out))
            line = line.replace("in1", str(in1))
            line = line.replace("in2", str(in2))
            program += line
        return program

    def _execute(self, genes, x):
        self._reset_reg(x)
        reg = self.registers
        for instr in genes:
            opcode, out, in1, in2 = self._decode_instr(instr)
            exec(self.primitives[opcode][1])
        return reg[0]

    def _reset_reg(self, x):
        for i in range(len(self.registers)):
            self.registers[i] = 1
        for i in range(len(x)):
            self.registers[i] = x[i]

    def _decode_instr(self, instr):
        instr.opcode %= self.num_primitives
        instr.out_reg %= self.num_regs
        instr.in_reg1 %= self.num_regs
        instr.in_reg2 %= self.num_regs
        return instr.opcode, instr.out_reg, instr.in_reg1, instr.in_reg2