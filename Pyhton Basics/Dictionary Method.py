

user = {
    "basket": [1, 2, 3],
    "greet": 'hello',
    'age': 20
}
print(user.get('age', 55))
user2 = dict(name='jonh')
print(user2)

print('basket' in user)
print('age' in user.keys())
print('hello' in user.keys())
print(user.items())
print(user.clear())
user.clear()
print(user)
