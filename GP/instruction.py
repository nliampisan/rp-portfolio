LARGEST_RAND = 100
import numpy as np

class Instruction:
    def __init__(self, code=None):
        if code == None:
            self.random()
        else:
            self.set(code)

    def set(self, code):
        self.opcode = code[0]
        self.out_reg = code[1]
        self.in_reg1, self.in_reg2 = code[2], code[3]

    def random(self):
        self.set(np.random.randint(LARGEST_RAND, size=4))

    def __str__(self):
        return "[" + str(self.opcode) + " " + str(self.out_reg) + " " + \
               str(self.in_reg1) + " " + str(self.in_reg2) + "]"