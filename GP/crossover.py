import random
# ----------------------------
# Base class: Crossover
# ----------------------------
class Crossover:
    def __init__(self, pc):
        self.pc = pc

# ----------------------------
# Derived class: OnePointCrossover
# ----------------------------
class OnePointCrossover(Crossover):
    def __init__(self, pc):
        super().__init__(pc)

    def cross(self, p1, p2):
        rd = random.uniform(0, 1)
        if(rd < self.pc):
            cut_point = random.randint(1, p1.get_length() - 1)
            if p1.can_cross(p2,cut_point):
                p1.genes[cut_point:], p2.genes[cut_point:] = p2.genes[cut_point:], p1.genes[cut_point:]
        return p1, p2