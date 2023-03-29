# Matrix multiplication
# Write two functions that each multiply two square matrices,
# one without using the built-in numpy functions and the other - using numpy.
# The first problem is inputted with lists of size, each with size elements.
# The second task is fed with objects of type np.ndarray --- square matrices of the same size.

# The first function should return a list of lists and the second function should return np.array.

from typing import List
import numpy as np

def no_numpy_mult(first, second):
    """
    param first: list of "size" lists, each contains "size" floats
    param second: list of "size" lists, each contains "size" floats
    """
    # Find the length of the first list (the height of the matrix)
    new_matrix_rows = len(first)

    # Find the length of the first element of the second list (the width of the matrix)
    new_matrix_columns = len(second[0])

    new_matrix = [[0 for _ in range(new_matrix_columns)] for _ in range(new_matrix_rows)]

    for i in range(new_matrix_rows):
        for j in range(new_matrix_columns):
            current_cell_sum_cumulative = 0
            for r in range(len(second)):
                current_cell_sum_cumulative += first[i][r] * second[r][j]

            new_matrix[i][j] = current_cell_sum_cumulative


    return new_matrix

def numpy_mult(first, second):
    """
    param first: np.array[size, size]
    param second: np.array[size, size]
    """

    #YOUR CODE: please use numpy

    result = np.matmul(first, second)
    return result


a = no_numpy_mult([[2, -3, 1], [5, 4, -2]], [[-7, 5], [2, -1], [4, 3]])
print(a)

b = numpy_mult(np.array([[2, -3, 1], [5, 4, -2]]), np.array([[-7, 5], [2, -1], [4, 3]]))
print(b)

# [[-16  16]
#  [-35  15]]
