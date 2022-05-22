class ParameterSet:
    def __init__(self):  # Assign default parameters (can be changed after an object is created)
        # Problem-related parameters
        self.is_maximize = True  # Maximization problem or minimization problem

        # GA's parameters
        self.max_gen = 20  # Maximum number of generations
        self.pop_size = 20  # Population size

        # Individual-related parameters
        self.num_instrs = 10

        # Evaluator-related parameters
        self.num_regs = 8

        # Breeder-related parameters
        self.ts = 2  # Tournament size
        self.pc = 0.9  # Crossover rate
        self.pm = 0.1  # Mutation rate
        self.elitism = True  # Elitism

    def print(self):
        print("--------------------------")
        print("Parameter Setting:")
        if self.is_maximize is True:
            print("Problem: Maximization")
        else:
            print("Problem: Minimization")
        print("Maximum number of generations =", self.max_gen)
        print("Population size =", self.pop_size)
        print("Number of instructions (fixed) =", self.num_instrs)
        print("Number of registers =", self.num_regs)
        print("Tournament size =", self.ts)
        print("Crossover rate =", self.pc)
        print("Mutation rate =", self.pm)
        print("Elitism =", self.elitism)
        print("--------------------------")