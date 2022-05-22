from GP.instruction import Instruction
from GP.element import Element
DEFAULT_FITNESS = 0

class Individual:
    def __init__(self, chromosome_len):
        self.genes = [Element() for i in range(chromosome_len)]
        self.fitness = DEFAULT_FITNESS

    def get_length(self):
        return len(self.genes)

    def can_cross(self, p2, crossover_pt):
        if self.genes[crossover_pt].get_url() == p2.genes[crossover_pt].get_url():
            return True
        else:
            return False

    def random(self):
        for i in range(self.get_length()):
            self.genes[i].random()

    def is_better_than(self, other):
        return self.fitness > other.fitness  # Suppose "the larger fitness, the better individual" is true.

    def __str__(self):
        return "gene = " + "".join(str(g) for g in self.genes) + ", fit = " + str(format(self.fitness, "10.4f"))