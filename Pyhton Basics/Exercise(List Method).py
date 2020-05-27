# using this list,
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# 1. Remove the Banana from the list
basket.remove("Banana")
print(basket)
# 2. Remove "Blueberries" from the list.
basket.pop(2)
print(basket)
# 3. Put "Kiwi" at the end of the list.
new_list = basket.append("kiwi")
print(new_list)
print(basket)
# 4. Add "Apples" at the beginning of the list
new_list = basket.insert(0, "Apples")
print(new_list)
print(basket)
# 5. Count how many apples in the basket
print(basket.count("Apples"))
# 6. empty the basket
basket.clear()
print(basket)
