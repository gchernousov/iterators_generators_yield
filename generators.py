def flat_generator(item_list):
    """Генератор, принимающий список списков и возвращающий плоское представление"""
    cursor = 0
    inner_cursor = 0
    while cursor < len(item_list):
        while inner_cursor < len(item_list[cursor]):
            yield item_list[cursor][inner_cursor]
            inner_cursor += 1
        else:
            cursor += 1
            inner_cursor = 0


def check_element_list(item, result = []):
    """Генератор, принимающий список с любым уровнем вложенности и возвращающий плоское представление"""
    count = 0
    while count < len(item):
        if type(item[count]) is list:
            check_element_list(item[count])
            count += 1
        else:
            result.append(item[count])
            count += 1
    else:
        return result

def flat_generator_infinite(item_list):
    flat_item_list = check_element_list(item_list)
    cursor = 0
    while cursor < len(flat_item_list):
        yield flat_item_list[cursor]
        cursor += 1


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]
]

complex_list = [
    [900, False, ['Moon', 'John', 8, ['ST-7', 119]], [7.92, 100, 'Harry']],
    [120, ['cat', None, 'oil', 5], 'KING', ['Earth', 'rabbit', 73164]],
    [[8, True], ['carry', ['burger', 'salt', 1000], 'SQL', 333], 5.25],
    [[12500, 'fail', 3.75, 816], 45, ['ZERO', 12.876, ['G-10', 'H-8', 77], 10, 'LOST'], '777'],
    [801, ['K-22', 5.82, '%%%', ['system()', 'KARL', 61834, 0.8]], 312, 6],
    48,
    ['YES', 77, 'Japan']
]


if __name__ == "__main__":

    # Работа flat_generator():

    print("Результат for in:\n")

    for item in flat_generator(nested_list):
        print(item)

    print("\nРезультат list comprehension:\n")

    flat_list = [item for item in flat_generator(nested_list)]
    print(flat_list)

    print("\n---------------------\n")

    # Работа FlatIteratorInfinite:

    print("Результат for in:\n")

    for item in flat_generator_infinite(complex_list):
        print(item)

    print("\nРезультат list comprehension:\n")

    flat_list = [item for item in flat_generator_infinite(complex_list)]
    print(flat_list)