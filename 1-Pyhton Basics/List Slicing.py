# List
amazon_cart = [
    'nootbooks',
    'sunglasses',
    'toys',
    'grapes'
]
# List are Mutable/changable
amazon_cart[0] = 'laptops'
print(amazon_cart)
# create copy of list  / instead of changing main list
amazon_cart[0] = 'laptops'
new_cart = amazon_cart[:]
new_cart[0] = 'Gum'

print(new_cart)
print(amazon_cart)

# Exercise
# Before you clikc RUN, guess the output of each print statement!
new_list = ['a', 'b', 'c']
print(new_list[1])
print(new_list[-2])
print(new_list[1:3])
new_list[0] = 'z'
print(new_list)

my_list = [1, 2, 3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list)
print(bonus)
