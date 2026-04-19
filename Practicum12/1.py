def pownum(a, n):
    '''
    Function finds the number a to the power of n
    '''
    if n == 0:
        return 1
    else:
        return a * pownum(a, n - 1)
    

print(pownum(3, 3))
