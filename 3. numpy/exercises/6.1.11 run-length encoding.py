import numpy as np

def encode(a):
    elements = []
    element_count = []
    last_elem = None
    count = 0

    for element_idx, current_elem in enumerate(a):
        if element_idx == 0:
            last_elem = current_elem

        if current_elem == last_elem:
            count += 1
        else:
            elements.append(last_elem)
            element_count.append(count)
            last_elem = current_elem
            count = 1

    elements.append(last_elem)
    element_count.append(count)
    return (np.array(elements), np.array(element_count))

a = np.array([1, 2, 2, 3, 3, 1, 1, 5, 5, 2, 3, 3])
print(encode(a))
