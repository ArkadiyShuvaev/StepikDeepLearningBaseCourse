def get_refined_elements(input: list) -> list:
    result = []

    for item in input:
        item_members = item.split()
        refined_members = [s for s in item_members if s.isalpha()]
        new_item = " ".join(refined_members)
        result.append(new_item)

    return result



input = ['1 thousand devils', 'My name is 9Pasha', 'Room #125 costs $100', '888']
refined_input = get_refined_elements(input)

expected = ['thousand devils', 'My name is', 'Room costs', '']
assert refined_input == expected, "Something is wrong! Please try again"

print(refined_input)
