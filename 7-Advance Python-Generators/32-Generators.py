# range is generator that why its iterable
# list is iterable but not a generator
def generator_func(num):
    for i in range(num):
        yield i*2


g = generator_func(100)
print(next(g))
# for item in generator_func(100):
#     print(item)


# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result


# my_list = make_list(100)
# print(my_list)
