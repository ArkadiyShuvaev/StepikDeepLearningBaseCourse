# Your task is to write a python function that takes as an argument:
# - a numerical function f, for which it is necessary to calculate
#   the derivative
# - the number ε. It must be used as a "small deviation" for the
#   approximate calculation of the derivative.

# The function must in turn return a numerical function f′ equal
# to the derivative of the function f.

from typing import Callable


def numerical_derivative_1d(func: Callable[[float], float], epsilon: float):
    """
    return a numerical function f' equal to the derivative of the function f
    :param func: float a numerical function f, for which it is necessary to
    calculate the derivative
    :param epsilon: float the number ε.
    :return: a numerical function f' equal to the derivative of the function f
    """
    def deriv_func(x: float):
        """
        :param x: float — точка, в которой нужно вычислить производную
        :return: приближённое значение производной в этой точке
        """
        return (func(x + epsilon) - func(x))/epsilon

    return deriv_func


def test_func(x: float) -> float:
    # x^2 +10x
    return x**2 + 10.0*x


deriv_func = numerical_derivative_1d(test_func, .01)
print(deriv_func(2))
