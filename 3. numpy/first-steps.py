import numpy as np

arr = np.array([1, 2, 3], dtype="int64")
# print(type(arr))
# print(set(dir(arr)) - set(dir(object)))
# print(arr.nbytes) # 64/8 * 3 = 24

# np.lookfor("mean value for array") # look for a method in the numpy documentation
# help(np.ma.mean)
# print(arr.mean()) # 2


# arr2 = np.array([[[1, 2, 3, 4],
#                 [2, 3, 4, 3],
#                 [1, 1, 1, 1]], 
#                 [[1, 2, 3, 4],
#                 [2, 3, 4, 3],
#                 [1, 1, 1, 1]]])
# print("len:", len(arr2), "-- количество элементов по первой оси.",
#       "\nsize:", arr2.size, "-- всего элементов в матрице.",
#       "\nndim:", arr2.ndim, "-- размерность матрицы.",
#       "\nshape:", arr2.shape, "-- количество элементов по каждой оси.")


# print(arr[-1]) # the last element: 3

# for i in arr:
#       print(i)

# arr3 = np.array([2, 3, 5, 7], dtype="int32")
# print(type(arr3))
# print(arr3.dtype)
# print(arr3.shape)
# print(arr3.nbytes)
# print(len(arr3))

# arr_zeros = np.zeros(7)
# print(arr_zeros)
# print(arr_zeros.dtype) # float64

# arr_ones = np.ones(7, dtype="int16")
# print(arr_ones)
# print(arr_ones.dtype) # int16

# arr2_zeros = np.zeros_like(arr_ones)
# print(arr2_zeros)
# print(arr2_zeros.dtype) # int16 !!!!

# arr = np.arange(1, 16, 4)
# print(arr) # 1, 5, 9, 13
# arr2 = np.arange(1, 5)
# print(arr2) # 1, 2, 3, 4
# arr3 = np.arange(5)
# print(arr3) # 0, 1, 2, 3, 4
# arr4 = np.arange(1., 3, 1)
# print(arr4) # 1., 2.

# arr = np.linspace(1, 15, 2)
# print(arr) # 1, 15

# arr2 = np.linspace(5, 12, 10)
# print(arr2) # [ 5. 5.77777778  6.55555556  7.33333333  8.11111111  8.88888889 9.66666667 10.44444444 11.22222222 12. ]


# arr3 = np.linspace(10, 32, 12)
# print(arr3) # [10. 12. 14. 16. 18. 20. 22. 24. 26. 28. 30. 32.]
# print(arr3[1] - arr3[0]) # 2

# arr = np.logspace(0, 3, 5) # 10^0, 10^3, step: 5
# print(arr) # [ 1. 5.62341325 31.6227766 177.827941 1000. ]

# print(np.log10(a))
# print(type(np.cos))

a = np.linspace(3, 33, 11)
b = np.linspace(-2, -22, 11)

# print(a)
# print(b)
# print("\n")

# # print(a + b)
# # print(a - b)
# # print(a * b)
# # print(a / b)

# print(5 * a) # 5 - scalar 
# print(2 ** a) 
# print(a ** 2)
# print(a > b)
# print(a >= 10)

# c = np.arange(0., 20)
# c_copy = np.copy(c)

# print(np.any(c == 0.), np.all(c)) # np.all(c) -> np.all(c != 0.)
# # True False

# # Inplace operations
# c += 1
# # print(c) # [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13. 14. 15. 16. 17. 18. 19. 20.]
# c_copy /= c
# print(c_copy) # [0. 0.5 0.66666667 0.75 0.8 0.83333333 ..... 0.95 ]

# # Constants
# print(np.pi)
# print(np.e)

# b = np.arange(1, 5, 1)
# print(b)          # [1 2 3 4]
# print(b.cumsum()) # [ 1  3  6 10 ]

# Sorting
# print(np.sort(b))
# b.sort()  # Inplace sorting
# print(b)

# Merging/Stacking arrays
# a = np.zeros(2)
# b = np.ones(2)
# c = np.hstack((a, b))
# print(c)   # [0. 0. 1. 1.]
# d = (a, b)
# print(d)   # (array([0., 0.]), array([1., 1.])

# # Append, delete, insert - create new array
# a = np.ones(5)                   # [1. 1. 1. 1. 1.]
# a = a.cumsum()  
# print(a)                         # [1. 2. 3. 4. 5.]
# print(np.append(a, [2, 3]))      # [1. 2. 3. 4. 5. 2. 3.]
# print(np.delete(a, [0, 2, 4]))   # [2. 4.] ([0, 2, 4] - array indexes)
# print(np.insert(a, 3, [-1, -2])) # [ 1.  2.  3. -1. -2.  4.  5.] (3 - array index)

# a = np.ones(5)
# a = a.cumsum() # [1. 2. 3. 4. 5.]
# print(a[::-1]) # [5. 4. 3. 2. 1.]
# print(a)       # [1. 2. 3. 4. 5.]
# b = a[::-1]    # the array "b" still referes to the array "a"

# b = a.copy()   # a new memory allocation

# Task #3
# a = np.linspace(start=-4*np.pi, stop=4*np.pi, num=100)
# sum2 = np.cos(a)**2 + np.sin(a)**2
# print(sum2)
# print(np.all(sum2))

# two-dimensional arrays
a = np.array([[1, 2], [2, 3]])
# print("len:", len(a), "-- количество элементов по первой оси.",       # 2
#       "\nsize:", a.size, "-- всего элементов в матрице.",             # 4
#       "\nndim:", a.ndim, "-- размерность матрицы.",                   # 2
#       "\nshape:", a.shape, "-- количество элементов по каждой оси.")  # (2, 2)

# print(a[1, 1]) # 3
# print(a[1][1]) # 3

b = np.arange(0, 20)
b.shape = (2, 10)
print(b)          # [[ 0  1  2  3  4  5  6  7  8  9] [10 11 12 13 14 15 16 17 18 19]]
