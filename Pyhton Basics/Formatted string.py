name = "Afra"
age = 21
print('Hi ' + name + '.You are ' + str(age) + ' Years old')

# formated 1  easy format
print(f'Hi {name}!You are {age} Years old')
# formated 2
print('Hi {}!You are {} Years old'.format(name, age))

# formated 3
print('Hi {0}!You are {1} Years old'.format(name, age))
# formated 4
print("Hello {name}, your age is {age}.".format(
    name="Cindy", age=50))
