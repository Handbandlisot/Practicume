def degree5(n):
    '''
    Function calculates what power of 5 the natural number n is
    '''
    if n == 1:
        return 0
    elif n % 5 != 0:
        return -1
    elif degree5(n // 5) == -1:
        return -1
    else:
        return 1 + degree5(n // 5)
    

print(degree5(1635))
