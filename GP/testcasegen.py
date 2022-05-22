import numpy as np

from GP.testcase import TestCase


class TestCaseGenerator:
    def __init__(self, fn):
        self.fn = fn

    def generate(self, num_test_cases):
        test_case_list = []
        for i in range(num_test_cases):
            x, y = self._gen_a_test_case()
            test_case_list.append(TestCase(x, y))
        return test_case_list

    def _gen_a_test_case(self):
        num_vars = self.fn.get_num_var()
        x = np.zeros(num_vars)
        for i in range(len(x)):
            x[i] = np.random.uniform(self.fn.domain[i][0], self.fn.domain[i][1])
        y = self.fn.evaluate(x)
        return x, y