basket = [1, 2, 3, 4, 5]

# adding
new_list = basket.append(100)
print(new_list)
print(basket)
# insert
new_list = basket.insert(4, 100)
print(new_list)
print(basket)
# extends
new_list = basket.extend([3, 100])
print(basket)
print(new_list)

# reemove
basket.pop()  # rmv end of the list
basket.pop(0)  # rmv item of index 0
print(basket)
# remove value
basket.remove(2)
print(basket)
# clear the list
new_list = basket.clear()
