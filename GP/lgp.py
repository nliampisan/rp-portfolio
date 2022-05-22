import time
from copy import deepcopy

from GP.breeder import Breeder
from GP.evaluator import Evaluator
from GP.mutator import Mutator
from GP.parameterset import ParameterSet
from GP.population import Population
from GP.selector import *
from GP.crossover import *
import matplotlib.pyplot as plt

class LGP:
    def __init__(self, params=ParameterSet()):
        # Create evaluator
        self.evaluator = Evaluator()
        self.gen_list = list()
        self.bsf_list = list()
        # Parameter settings
        self.params = params

        # Create breeder
        selector = TournamentSelector(params.ts)
        crossover = OnePointCrossover(params.pc)
        mutator = Mutator(params.pm)
        self.breeder = Breeder(selector, crossover, mutator, params.elitism)

    def _reset(self):
        self.gen = 0
        self.best_so_far = None
        self.pop1 = Population(self.params.pop_size, self.params.num_instrs)
        self.pop2 = Population(self.params.pop_size, self.params.num_instrs)

    def _update_best_so_far(self, pop):
        current_best = pop.get_best_indiv()
        if self.best_so_far == None:
            self.best_so_far = deepcopy(current_best)
        elif current_best.is_better_than(self.best_so_far):
            self.best_so_far = deepcopy(current_best)

    def run(self):
        # Reset state
        self._reset()

        # Loop
        for self.gen in range(self.params.max_gen):
            # Evaluate current population
            self.evaluator.eval_pop(self.pop1)
            print("--------------------------")
            print("Generation:", self.gen)
            self.pop1.print()

            # Check best-so-far individual
            self._update_best_so_far(self.pop1)
            print("Best-so-far:", self.best_so_far)

            self.gen_list.append(self.gen)
            self.bsf_list.append(self.best_so_far.fitness)

            # Breed offspring population
            self.breeder.breed(self.pop1, self.pop2)

            # Swap population
            self.pop1, self.pop2 = self.pop2, self.pop1

            # Delay
            time.sleep(0.5)
            self.plot_stats()

        return self.best_so_far

    def plot_stats(self):
        # Update list
        # Clear figure and re-plot
        plt.plot(self.gen_list, self.bsf_list, label='Best-so-far')
        # plt.errorbar(gen_list, avg_list, sd_list, label = 'Avg & SD')

        # Graph settings
        ax = plt.gca()  # Get current axis
        ax.set_xlim(xmin=-0.5, xmax=self.params.max_gen)
        # ax.set_xticks(gen_list, minor = True)      # Set x-ticks according to generations
        ax.set_xticks(self.gen_list)  # Set x-ticks according to generations
        ax.grid()  # Show grid
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        ax.set_title("Genetic Algorithm")
        ax.set_ylabel('Fitness')
        ax.set_xlabel('Generation')

        # Show and pause
        plt.show()
