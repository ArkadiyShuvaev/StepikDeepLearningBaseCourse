from math import sqrt
import numpy as np


def grad_descent_v2(func, deriv, low: float, high: float, callback=None):
    """
    Реализация градиентного спуска для функций с несколькими
    локальным минимумами, но с известной окрестностью глобального минимума.
    Все тесты будут иметь такую природу.
    :param func: float -> float — функция
    :param deriv: float -> float — её производная
    :param low: float — левая граница окрестности
    :param high: float — правая граница окрестности
    :param callback: callalbe -- функция логирования
    """
    sub_range_count = 6
    iteration_count_each_sub_range = 10
    sub_range_results = list()

    class CalculationResult(object):
        def __init__(self, x_value, func_value):
            self.x_value = x_value
            self.func_value = func_value

        def __lt__(self, other):
            return self.func_value < other.func_value

    def find_local_min(func, deriv, low_local, high_local, iters=5000,
                       lr=0.05) -> CalculationResult:
        # функция для нахождения минимума функции f на промежутке
        # (low_local, high_local)
        learning_rate = lr
        number_of_iterations = iters
        iteration_number = 0

        # the max number of attempts to get out of range between low_local and high_local values
        allowed_border_hits = 10
        border_hit_count = 0

        x = np.random.uniform(low_local, high_local)
        func_value = func(x)

        while iteration_number < number_of_iterations:
            derivative_value = deriv(x)
            func_value = func(x)
            iteration_number += 1

            if callback is not None:
                callback(x, func_value)

            if derivative_value == 0:
                break
            else:
                # new_x = x - learning_rate * derivative_value
                if derivative_value > 0:
                    x = \
                        x - learning_rate * 1/np.sqrt(iteration_number)
                else:
                    x = \
                        x + learning_rate * 1/np.sqrt(iteration_number)

                if x < low_local:
                    x = low_local
                    border_hit_count += 1

                if x > high_local:
                    x = high_local
                    border_hit_count += 1

                if border_hit_count > allowed_border_hits:
                    break

        result = CalculationResult(x, func_value)
        return result

    def find_sub_range_min(func, deriv, low_local, high_local,
                   iteration_count_each_sub_range) -> CalculationResult:
        local_iteration_results = []

        for i in range(0, iteration_count_each_sub_range):
            local_min_value = find_local_min(func, deriv, low_local,
                                             high_local)
            local_iteration_results.append(local_min_value)

        local_iteration_results.sort()
        best_sub_range = local_iteration_results[0]

        return best_sub_range

    sub_ranges = np.linspace(low, high, sub_range_count)

    for i in range(0, sub_range_count - 1):
        low_local = sub_ranges[i]
        high_local = sub_ranges[i + 1]

        sub_range_value = find_sub_range_min(func, deriv, low_local, high_local,
                                                   iteration_count_each_sub_range)

        sub_range_results.append(sub_range_value)

    sub_range_results.sort()
    best_estimate = sub_range_results[0]

    return best_estimate.x_value


def test_func(x: float) -> float:
    result = 0.0
    try:
        result = 5 * np.abs(x)/x**2 - 0.5 * x + 0.1 * np.sqrt(-x) + 0.01 * x**2
    except:
        print(x)
    return result

def deriv(x: float) -> float:
    # 2x + 10
    # return 2*x + 10.0
    return -0.5 - 0.05/np.sqrt(-x) + 0.02 * x + 5/(x * np.abs(x)) - (10 * np.abs(x))/x**3


value = grad_descent_v2(test_func, deriv, -4, -2, callback=None)

print(value)
