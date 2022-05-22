import random


# ----------------------------
# Base class: Selector
# ----------------------------
class Selector:
    def select(self, pop):  # Just random selection
        size = pop.get_pop_size()
        rd = random.randint(0, size - 1)
        return pop.indivs[rd]


# ----------------------------
# Derived class: TournamentSelector
# ----------------------------
class TournamentSelector(Selector):
    def __init__(self, tournament_size):
        super().__init__()
        self.ts = tournament_size

    def select(self, pop):
        size = pop.get_pop_size()
        rd = random.randint(0, size - 1)
        best_idx = rd;

        for i in range(1, self.ts):
            rd = random.randint(0, size - 1)
            if pop.indivs[rd].is_better_than(pop.indivs[best_idx]):
                best_idx = rd;

        return pop.indivs[best_idx]
# ----------------------------