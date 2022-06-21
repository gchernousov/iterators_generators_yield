class FlatIterator:
    """Итератор, принимающий список списков и возвращающий плоское представление"""

    def __init__(self, new_list):
        self.new_list = new_list
        self.cursor = 0
        self.inner_cursor = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor <= len(self.new_list) -1:
            if self.inner_cursor < len(self.new_list[self.cursor]) -1:
                self.inner_cursor += 1
                return self.new_list[self.cursor][self.inner_cursor]
            else:
                if self.cursor < len(self.new_list) -1:
                    self.cursor += 1
                    self.inner_cursor = -1
                    if self.inner_cursor < len(self.new_list[self.cursor]):
                        self.inner_cursor += 1
                        return self.new_list[self.cursor][self.inner_cursor]
                else:
                    raise StopIteration
        else:
            raise StopIteration


class FlatIteratorInfinite:
    """Итератор, принимающий список с любым уровнем вложенности и возвращающий плоское представление"""

    def __init__(self, item_list):
        self.item_list = self.check_list(item_list)
        self.cursor = 0

    def check_list(self, i_list, result=[]):
        count = 0
        while count < len(i_list):
            if type(i_list[count]) is list:
                self.check_list(i_list[count])
                count += 1
            else:
                result.append(i_list[count])
                count += 1
        else:
            return result

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor < len(self.item_list):
            self.cursor += 1
            return self.item_list[self.cursor -1]
        else:
            raise StopIteration


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

    # Работа FlatIterator:

    print("Результат for in:\n")

    for item in FlatIterator(nested_list):
        print(item)

    print("\nРезультат list comprehension:\n")

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    print("\n---------------------\n")

    # Работа FlatIteratorInfinite:

    print("Результат for in:\n")

    for item in FlatIteratorInfinite(complex_list):
        print(item)

    print("\nРезультат list comprehension:\n")

    flat_list = [item for item in FlatIteratorInfinite(complex_list)]
    print(flat_list)