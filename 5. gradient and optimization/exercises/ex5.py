# In this task, you should find the minimum of a function using gradient descent.

# You are given the func function, its derivative deriv (*), as well as the initial point start, as an input, and the local minimum point as an output. For your convenience, we have written a function to draw the gradient descent path.
# (*) - you will not need to calculate the derivative.

# In the first implementation of gradient descent, you can assume that the inputs are functions with a single, global minimum. Before writing code, ask yourself the following questions:

# How do you know when it's time to stop? This may depend on the gradient or distance between two adjacent steps of the algorithm, as well as on the number of iterations already performed.
# How to correctly change the step size (learning rate) from iteration to iteration?
# At this point, it is guaranteed that there is a solution using conventional gradient descent with a fixed learning rate and a predetermined number of iterations.

import numpy as np


def grad_descent_v1(f, deriv, x0=None, lr=0.1, iters=100, callback=None):
    """
    Реализация градиентного спуска для функций с одним локальным минимумом,
    совпадающим с глобальным. Все тесты будут иметь такую природу.
    :param func: float -> float — функция
    :param deriv: float -> float — её производная
    :param x0: float — начальная точка
    :param lr: float — learning rate
    :param iters: int — количество итераций
    :param callback: callable — функция логирования
    """
    number_of_iterations = iters
    current_iteration_number = 0
    learning_rate = lr
    # current_proximity_to_zero = proximity_to_zero

    if x0 is None:
        # Если точка не дана, сгенерируем случайную
        # из равномерного распределения.
        # При таком подходе начальная точка может быть
        # любой, а не только из какого-то ограниченного диапазона
        # np.random.seed(179)
        x0 = np.random.uniform()

    x = x0

    while current_iteration_number < number_of_iterations:
        derivative_value = deriv(x)
        current_iteration_number += 1

        if callback is not None:
            callback(x, f(x))

        if derivative_value == 0:
            break
        else:
            x = x - learning_rate * derivative_value

    return x


def test_func(x: float) -> float:
    # x^2 +10x
    return x**2 + 10.0*x


def deriv(x: float) -> float:
    # 2x + 10
    return 2*x + 10.0


value = grad_descent_v1(test_func, deriv, x0=None, lr=0.1, iters=100,
                        callback=None)

print(value)
