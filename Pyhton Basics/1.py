
from datetime import datetime
a = datetime.now()
a = int(a.strftime('%Y'))
print(type(a))

birthyear = int(input('What year were you born??'))
print(type(birthyear))

age = a - birthyear
print(f'You are  {age}  years old')
