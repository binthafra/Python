print(4 > 5)
print(4 == 5)
print(4 == 4)
print('a' > 'A')
print('a' > 'b')
print(0 >= 0)
print(45 != 4)
print(not(True))


# Exercise
is_magician = False
is_expert = True
# check if magician ANd expert :"ypu are a master magician"
if is_expert and is_magician:
    print("your are a master magician")
# check if magician but not expert:"at least you're getting there"
elif is_magician and not is_expert:
    print("at least you're getting there")
# if you're not a magician: "You need magic power"
elif not is_magician:
    print("You need magic power")
