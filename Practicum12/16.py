def ten_to_n(x, n):
    '''
    Function converts natural numbers x 
    from the decimal number system to the n-ary number system
    '''
    if x == 0:
        return ''
    return ten_to_n(x // n, n) + str(x % n)


print(ten_to_n(25, 5))
