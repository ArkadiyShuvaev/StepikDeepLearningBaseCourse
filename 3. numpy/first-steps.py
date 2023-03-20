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

arr = np.linspace(1, 15, 2)
print(arr) # 1, 15

arr2 = np.linspace(5, 12, 10)
print(arr2) # [ 5. 5.77777778  6.55555556  7.33333333  8.11111111  8.88888889 9.66666667 10.44444444 11.22222222 12. ]