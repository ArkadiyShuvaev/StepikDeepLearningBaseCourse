def cumulative_sum_and_erase(input_array: list, erase = 1) -> list:
    result = []
    cumulative_value = 0

    for current_value in input_array:
        cumulative_value += current_value
        if cumulative_value != erase:
            result.append(cumulative_value)

    return result


a = [5, 1, 4, 5, 14]
B = cumulative_sum_and_erase(a, erase=10)

assert B == [5, 6, 15, 29], "Something is wrong! Please try again"