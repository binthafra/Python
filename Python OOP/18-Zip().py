my_list = [1, 2, 3]
your_list = [10, 20, 30]
her_list = (0, 100, 110)


def multipy_by2(item):
    return item*2


def only_even(item):
    return item % 2 == 0


print(list(zip(my_list, your_list, her_list)))
print(my_list)
