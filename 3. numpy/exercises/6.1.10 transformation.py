import numpy as np

def transform(X, a=1):
    """
    param X: np.array[batch_size, n]
    """
    arr = np.copy(X)
    row_count = len(X)
    col_count = len(X[0])
    res = np.zeros(shape = (row_count, col_count * 2))

    temp_row = np.zeros(shape=(1, col_count))
    for row_idx, row in enumerate(X):
        for elem_idx, elem in enumerate(row):
            e = elem_idx, elem
            new_idx = col_count - 1 - elem_idx
            if elem_idx % 2 == 0:
                temp_row[0, new_idx] = pow(elem, 3)
            else:
                temp_row[0, new_idx] = a
        concatenated_row = np.concatenate((arr[row_idx, ], temp_row[0, ]))
        res[row_idx, ] = np.copy(concatenated_row)

    return res


x = np.array([[1,2,3,4,5], [100,200,300,400,500]])
res = transform(x)
print(res)
