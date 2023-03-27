import numpy as np

# x = np.arange(64).reshape(8, 2, 4)
# print(x)
# # [[[ 0  1  2  3]
# #   [ 4  5  6  7]]
# #
# #  [[ 8  9 10 11]
# #   [12 13 14 15]]
# #
# #  [[16 17 18 19]
# #   [20 21 22 23]]
# #
# #  [[24 25 26 27]
# #   [28 29 30 31]]
# #
# #  [[32 33 34 35]
# #   [36 37 38 39]]
# #
# #  [[40 41 42 43]
# #   [44 45 46 47]]
# #
# #  [[48 49 50 51]
# #   [52 53 54 55]]
# #
# #  [[56 57 58 59]
# #   [60 61 62 63]]]

# # Print the shape, length, size, and number of dimensions of x
# print("shape: ", x.shape, "len: ", len(x), "size: ", x.size, "ndim: ", x.ndim)
# # shape:  (8, 2, 4) len:  8 size:  64 ndim:  3

# x = np.arange(64).reshape(8, 2, 4) # create a 3D array with shape (8,2,4)
# print(np.sum(x)) # sum all elements in x

# print(np.sum(x, axis=0)) # sum all elements along axis 0
# print(np.sum(x, axis=1)) # sum all elements along axis 1
# print(np.sum(x, axis=2)) # sum all elements along axis 2
# print(np.sum(x, axis=(1, 2))) # sum all elements along axis 1 and 2


# # LINEAR ALGEBRA
# a = np.array([[2, 1], [2, 3]])
# print(a)
# # [[2 1]
# #  [2 3]]
# print(np.linalg.det(a))
# # 4.0 (2 * 3 - 2 * 1) = 4

# # find the inverse of the matrix
# b =np.linalg.inv(a)
# print(b)
# # [[ 0.75 -0.25]
# #  [-0.5   0.5 ]]

# print(a.dot(b)) # print(a.dot(b)) == print(b.dot(a))
# # [[1. 0.]
# #  [0. 1.]]
# print(b.dot(a))
# # [[1. 0.]
# #  [0. 1.]]

