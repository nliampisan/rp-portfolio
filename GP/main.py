# Create a set of parameters
from GP.function import TestFunction1D
from GP.lgp import LGP
from GP.parameterset import ParameterSet
from GP.testcasegen import TestCaseGenerator
import matplotlib.pyplot as plt
import random
# import timeit
# starttime = timeit.default_timer()
# print("The start time is :",starttime)

random.seed(1)
params = ParameterSet()
# Adjust some parameters
params.is_maximize = True
params.max_gen = 2
params.pop_size = 4
params.num_instrs = 5
# Verify parameters
params.print()

# gen = TestCaseGenerator(fn=TestFunction1D())
# num_test_cases = 300
# test_cases = gen.generate(num_test_cases)
import matplotlib.pyplot as plt

# x = [tc.x for tc in test_cases]
# y = [tc.y for tc in test_cases]
# plt.scatter(x, y)
# plt.show()

# Create an LGP object
lgp = LGP(params)

# Then, run GA
best_indiv = lgp.run()

# Display result
print("\nThe best individual founded by GP:", best_indiv)
lgp.plot_stats()
# print("The time difference is :", timeit.default_timer() - starttime)
#The return value is seconds as a float.



# print("\nSolution:")
# program = lgp.evaluator.decode_indiv(best_indiv)
# print(program)

# r = []
# for tc in test_cases:
#     result = lgp.evaluator._execute(best_indiv.genes, tc.x)
#     r.append(result)
#
# import matplotlib.pyplot as plt
#
# x = [tc.x for tc in test_cases]
# y = [tc.y for tc in test_cases]
# plt.scatter(x, y)
# plt.show()
# plt.scatter(x, r)
# plt.show()
