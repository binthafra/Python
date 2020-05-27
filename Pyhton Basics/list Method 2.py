basket = ['a', 'b', 'c', 'd', 'e', 'd']
print(basket.index('d'))
# count
print(basket.count('d'))
# sort
# basket.sort()

print(sorted(basket))  # sorted create a copy not change the original
print(basket)
# reverse
basket.sort()
basket.reverse()
print(basket)
print(basket[::-1])  # reverse
print(basket)

# range
# print(list(range(1, 100)))  # range 1-99
# print(list(range(100)))  # range 0-99

# join
# sentence = " "
new_sentence = " ".join(["HI", "my", "name", "Is", "Afra"])
print(new_sentence)
