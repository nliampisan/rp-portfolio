import random
# ----------------------------
# Base class: Mutator
# ----------------------------
class Mutator:
    def __init__(self, pm):
        self.pm = pm

    def mutate(self, p):
        for i in range(p.get_length()):
            rd = random.uniform(0, 1)
            if rd < self.pm:
                p.genes[i].random()
        return p