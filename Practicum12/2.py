def count(n):
    '''
    Function calculates the number of digits of a natural number
    '''
    if n < 10:
        return 1
    else:
        return 1 + count(n // 10)


print(count(555))
