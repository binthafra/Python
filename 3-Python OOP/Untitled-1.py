

while True:
    try:
        age = int(input('whats is your age?'))
        print(age)
    except:
        print('please enter a number')
    else:
        print('Thank you')
        break
