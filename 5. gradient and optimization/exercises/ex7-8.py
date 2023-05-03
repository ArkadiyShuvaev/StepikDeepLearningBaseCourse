# Find a derivative of the function sin(xz)−y^2z+exp(x)

from math import sin, cos, tan, exp, sqrt, pi
import numpy as np


def grad_1(x, y, z):
    # возвращает кортеж из 3 чисел --- частных производных по x,y,z

    dx = z*cos(x*z) + np.exp(x)
    dy = -(2*z*y)
    dz = x*cos(x*z) - y**2
    return (dx, dy, dz)


# assert np.allclose(grad_1(1, 1, 1), (3.258584134327185, -2, -0.45969769413186023), atol=5e-6)
# assert np.allclose(grad_1(1, 8, 0), (2.718281828459045, 0, -63.0), atol=5e-6)
# assert np.allclose(grad_1(-11, pi, 1), (0.004442399688841031, -6.283185307179586, -9.918287078957917), atol=5e-6)


# Find a derivative of the function ψ(x,y,z)= ln(cos(exp(x+y)))−ln(xy)
def grad_2(x, y, z):
    # возвращает кортеж из 3 чисел --- частных производных по x,y,z
    dx = -(tan(exp(x+y)))/(x+y) - 1/x
    dy = -(tan(exp(x+y)))/(x+y) - 1/y
    dz = 0
    return (dx, dy, dz)


assert np.allclose(grad_2(1, 1, 0), (-15.73101919885423, -15.73101919885423, 0), atol=5e-6)
assert np.allclose(grad_2(-10, 3, 0), (0.09999916847105042, -0.3333341648622829, 0), atol=5e-6)
assert np.allclose(grad_2(15, 4, 0), (54654806.79650013, 54654806.6131668, 0), atol=5e-6)
