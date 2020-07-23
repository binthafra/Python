#iterable -list ,dict,tuple,set,string
# iterable ->ono by one check each item in the collection
user = {
    'name': "afra",
    'age': 20,
    'can_swim': False
}
# print only keys
for item in user:
    print(item)
for item in user.keys():
    print(item)

# print key and value
for item in user.items():
    print(item)
for item in user.values():
    print(item)


for key, value in user.items():
    print(key, value)
