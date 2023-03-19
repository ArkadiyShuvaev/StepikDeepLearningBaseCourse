def func(value):
    second_item = value[1]
    last_symbol = second_item[-1]
    return last_symbol

items = [('one', 'two'), ('three', 'four'), ('five', 'six'), ('string', 'a')]
sorted_items = sorted(items, key = func)

assert sorted_items == [('string', 'a'), ('one', 'two'), ('three', 'four'), ('five', 'six')], \
    "Something is wrong! Please try again"

print(sorted_items)
