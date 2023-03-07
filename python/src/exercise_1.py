def multiply_odd_values(N: int) -> tuple[int, int]:
    """ Returns the multiplication of all odd natural numbers not exceeding N
    """
    result = 1
    for i in range(1, N + 1, 2):
        result = result * i

    return result

N = 25
N_double_fact = multiply_odd_values(N)

assert N_double_fact == 7905853580625, "Something is wrong! Please try again"
print(N_double_fact)