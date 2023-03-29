import numpy as np

def cumsum(A):
    #param A: np.array[m,n]
    arr_height = len(A)
    res = np.zeros(shape=(arr_height, len(A[0])))
    cum_sum = 0

    for i in range(arr_height):
        row = A[i, : ]
        cum_sum = np.cumsum(row, dtype="float64")
        res[i] = np.array(cum_sum)

    return res

a = np.array([[1,2,3], [4,5,6]])
c = cumsum(a)
print(c)