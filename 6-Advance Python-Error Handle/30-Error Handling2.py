def sum(n1, n2):
    try:
        return n1+n2
    except TypeError as err:
        print(f"please enter number {err}")


print(sum(1, '2'))
# anoter error handle


def sum(n1, n2):
    try:
        return n1/n2
    except (TypeError, ZeroDivisionError)as err:
        print(err)


print(sum(1, 0))
