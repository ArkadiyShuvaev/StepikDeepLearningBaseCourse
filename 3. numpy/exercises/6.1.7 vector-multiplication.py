# You are given two vectors a and b in three-dimensional space. Implement their scalar product with and without numpy

import numpy as np

def no_numpy_scalar(v1, v2):
    #param v1, v2: lists of 3 ints
    #YOUR CODE: please do not use numpy
    result = 0
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    return result

def numpy_scalar (v1, v2):
    #param v1, v2: np.arrays[3]
    #YOUR CODE

    result = np.dot(v1, v2)
    return result


a = no_numpy_scalar([1, 2, 1], [2, 6, 1])
print(a)
# 15

b = numpy_scalar([1, 2, 1], [2, 6, 1])
print(b)

