from functools import reduce

class Neuron:
    weights: list
    activation_function: lambda x: x
    last_forward_list: list

    def __init__(self, w: list, f = lambda x: x):
        self.weights = w.copy()
        self.activation_function = f
        self.last_forward_list = None


    def forward(self, x: list):
        self.last_forward_list = x
        zipped_list = zip(self.weights, x)

        result = 0
        for item in zipped_list:
            result += item[0] * item[1]

        return self.activation_function(result)

    def backlog(self):
        return self.last_forward_list


neuron = Neuron([1, 2, 3])
print(neuron.forward([3, 4, 5]))
print(neuron.backlog())
