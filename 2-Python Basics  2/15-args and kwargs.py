def super_func(*args, **kwargs):
    print(args)
    print(kwargs)
    return sum(args)


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))

# 2


def super_funct(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    print(args)
    print(kwargs)
    return sum(args) + total


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))
