

while True:
    try:
        age = int(input('whats is your age?'))
        10/age
    except ValueError:
        print('please enter a number')
        continue
    except ZeroDivisionError:
        print('please enter age higher than 0')
        break
    else:
        print('Thank you')
        break
    finally:
        print('ok! i am finally done')
    print('can you hear me')
