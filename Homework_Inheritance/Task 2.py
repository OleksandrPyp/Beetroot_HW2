#Task 2 Mathematician
class Mathematician:

    def square_nums(self, some_list: list) -> list:
        sq_num = [x**2 for x in some_list]
        return sq_num

    def remove_positives(self, some_list: list) -> list:
        r_pos = [x for x in some_list if x < 0]
        return r_pos

    def filter_leaps(self, some_list: list) -> list:
        leaps = list(filter(lambda x: (x % 4 == 0), some_list))
        return leaps


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))

