from copy import deepcopy


class Breeder:
    def __init__(self, selector, crossover, mutator, elitism):
        self.selector = selector
        self.crossover = crossover
        self.mutator = mutator
        self.elitism = elitism

    def breed(self, parent_pop, offspring_pop):
        size = parent_pop.get_pop_size()

        count = 0
        while count < size:
            # selection
            p1 = deepcopy(self.selector.select(parent_pop))
            p2 = deepcopy(self.selector.select(parent_pop))

            # crossover
            q1, q2 = self.crossover.cross(p1, p2)

            # mutation
            o1 = self.mutator.mutate(q1)
            o2 = self.mutator.mutate(q2)

            # insert new individuals into the offspring popuation
            offspring_pop.indivs[count] = o1
            count += 1
            offspring_pop.indivs[count] = o2
            count += 1

        # elitist
        if self.elitism is True:
            offspring_pop.indivs[0] = deepcopy(parent_pop.get_best_indiv())