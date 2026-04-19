def check_divisor(x, d):
    if d * d > x:
        return 1
    if x % d == 0:
        return 0
    return check_divisor(x, d + 1)

def function1(x):
    '''
    Function determines whether a given natural number x is prime
    '''
    if x < 2:
        return 0
    if x == 2:
        return 1
    return check_divisor(x, 2)


print(function1(11))
