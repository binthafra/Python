from functools import reduce
my_list = [1, 2, 3]


def multipy_by2(item):
    return item*2


def only_even(item):
    return item % 2 == 0


def accumulator(acc, item):
    print(acc, item)
    return acc+item


print(reduce(accumulator, my_list, 100))
print(my_list)
