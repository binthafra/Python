my_list = [1, 2, 3]


def multipy_by2(item):
    return item*2


def only_even(item):
    return item % 2 == 0


print(list(filter(only_even, my_list)))
print(my_list)
