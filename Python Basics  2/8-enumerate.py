# i=index char=character
for i, char in enumerate('Hello'):
    print(1, char)
for i, char in enumerate([1, 2, 3, 4]):
    print(i, char)
# Exercise
for i, char in enumerate(list(range(100))):

    if char == 50:
        print(f"index of 50 is : {i}")
