import numpy as np

from GP.testcasegen import TestCaseGenerator
from GP.function import *


from math import sin, cos
primitives = [["ADD", "reg[out] = reg[in1] + reg[in2]"], \
              ["SUB", "reg[out] = reg[in1] - reg[in2]"], \
              ["MUL", "reg[out] = reg[in1] * reg[in2]"], \
              ["DIV", "if reg[in2] == 0:\n    reg[out] = 1\nelse:\n    reg[out] = reg[in1] / reg[in2]"], \
              ["SIN", "reg[out] = sin(reg[in1])"], \
              ["COS", "reg[out] = cos(reg[in1])"]]


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
        sum_sq_err = 0.0
        for tc in self.test_cases:
            y = self._execute(indiv.genes, tc.x)
            sum_sq_err += (tc.y - y) ** 2
            # indiv.fitness = float(-sum_sq_err / len(test_cases))
        indiv.fitness = float(-sum_sq_err)

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