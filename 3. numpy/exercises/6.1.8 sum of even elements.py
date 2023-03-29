# Create a function that finds the sum of even elements on the main diagonal of a square matrix
# (even elements, not elements at even positions!).
# If there are no even elements, return 0. Use the numpy library.

# What are masked arrays?
# Consider the following problem. You have a dataset with missing or invalid entries.
# If you’re doing any kind of processing on this data, and want to skip or flag these unwanted entries
# without just deleting them, you may have to use conditionals or filter your data somehow.
# The numpy.ma module provides some of the same funcionality of NumPy ndarrays
# with added structure to ensure invalid entries are not used in computation.

# From the Reference Guide:

# A masked array is the combination of a standard numpy.ndarray and a mask.
# A mask is either nomask, indicating that no value of the associated array is invalid,
# or an array of booleans that determines for each element of the associated array whether the value is valid or not.
# When an element of the mask is False, the corresponding element of the associated array is valid and is said to be unmasked.
# When an element of the mask is True, the corresponding element of the associated array is said to be masked (invalid).

# We can think of a MaskedArray as a combination of:
# - Data, as a regular numpy.ndarray of any shape or datatype;
# - A boolean mask with the same shape as the data;
# - A fill_value, a value that may be used to replace the invalid entries in order to return a standard numpy.ndarray.




import numpy as np

def diag_2k(a):
    #param a: np.array[size, size]
    diagonal = np.diag(a)
    result = diagonal[diagonal % 2 == 0].sum()
    return result

elements = np.linspace(0, 8, 9)
# [0. 1. 2. 3. 4. 5. 6. 7. 8.]
a = np.diag(elements)
print(a)

sum_of_even_elements = diag_2k(a)
print(sum_of_even_elements)