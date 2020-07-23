my_set = {1, 2, 3, 4, 5}
ur_set1 = {4, 5, 6, 7, 8, 9, 10}
print(my_set.difference(ur_set1))
print(my_set)
# print(ur_set1.difference(my_set))

# print(my_set.discard(5))
print(my_set.difference_update(ur_set1))
print(my_set)

# Intersection
print(my_set.intersection(ur_set1))  # common things
print(my_set & ur_set1)

# isdisjoint
print(my_set.isdisjoint(ur_set1))  # tow circle are overlapping


# Union
print(my_set.union(ur_set1))  # set get together
print(my_set | ur_set1)

# isSubset
My_set = {4, 5}
yourset = {4, 5, 6, 7, 8, 9}
print(My_set.issubset(yourset))

# isSuperset
My_set = {4, 5}
yourset = {4, 5, 6, 7, 8, 9}
print(My_set.issuperset(yourset))
print(yourset.issuperset(My_set))
