from GP.individual import Individual


class Population:
    def __init__(self, size, num_instrs):
        self.indivs = [Individual(num_instrs) for i in range(size)]

    def get_pop_size(self):
        return len(self.indivs)

    def get_best_indiv(self):
        best = self.indivs[0]
        for i in self.indivs:
            if i.is_better_than(best):
                best = i
        return best

    def print(self):
        for p in self.indivs:
            print(p)