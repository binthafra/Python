# set  comprehension


my_list4 = {num**2 for num in range(0, 100)
            if num % 2 == 0}
print(my_list4)

#  dictionary comprehension
dictionary = {
    "a": 1,
    "b": 2
}
my_dict = {key: value**2 for key, value in
           dictionary.items()}
print(my_dict)


# another exercise
my_dict = {num: num*2 for num in [1, 2, 3]}
print(my_dict)
