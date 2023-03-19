import numpy as np

arr = np.array([1, 2, 3], dtype="int64")
# print(type(arr))
# print(set(dir(arr)) - set(dir(object)))
print(arr.nbytes) # 64/8 * 3 = 24

# np.lookfor("mean value for array") # look for a method in the numpy documentation
# help(np.ma.mean)
# print(arr.mean()) # 2


arr2 = np.array([[[1, 2, 3, 4],
                [2, 3, 4, 3],
                [1, 1, 1, 1]], 
                [[1, 2, 3, 4],
                [2, 3, 4, 3],
                [1, 1, 1, 1]]])
print("len:", len(arr2), "-- количество элементов по первой оси.",
      "\nsize:", arr2.size, "-- всего элементов в матрице.",
      "\nndim:", arr2.ndim, "-- размерность матрицы.",
      "\nshape:", arr2.shape, "-- количество элементов по каждой оси.")


