print(list(map(lambda num: num**2, [5, 4, 3])))


a = [(0, 2), (5, 2), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])

print(a)
