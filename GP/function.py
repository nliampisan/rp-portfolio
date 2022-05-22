# ----------------------------
# Base class: Function
# ----------------------------
class Function:
    def __init__(self):
        self.fn = "20 * np.sin(x[0]) + 10 * np.cos(x[1]) - 0.5 * x[0] * x[1]"  # Function (represetned as a string)
        self.domain = [[-3.0, 3.0], [3.0, 5.0]]

    def evaluate(self, x):
        return eval(self.fn)  # Convert string into expression and evaluate

    def get_num_var(self):
        return len(self.domain)

    def print(self):
        print("--------------------------")
        print("Function:", self.fn)
        print("Number of variables:", self.get_num_var())
        print("Domain:", self.domain)
        print("--------------------------")

    def __str__(self):
        return self.fn.replace("np.", "")  # To remove "np."


# ----------------------------
# Derived class: Simple1DFunction
# ----------------------------
class TestFunction1D(Function):
    def __init__(self):
        # self.fn = "np.sin(20 * np.pi * x) + np.cos(6 * np.pi * x)"
        # self.domain = [[-.5, .5]]
        self.fn = "x * x - x + 1"
        self.domain = [[-10, 10]]