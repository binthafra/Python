# list ,set ,disctioary
my_list = []

for char in "Hello":
    my_list.append(char)
print(my_list)


# another way
my_list = [char for char in "Hello"]
# for char in "Hello":
#     my_list.append(char)
print(my_list)

my_list2 = [num for num in range(0, 10)]
print(list(map(lambda num: num*2, my_list2)))

my_list3 = [num*2 for num in range(0, 10)]
print(my_list3)
my_list4 = [num**2 for num in range(0, 10)]
print(my_list4)
my_list5 = [num**2 for num in range(0, 10) if num % 2 == 0]
print(my_list5)
