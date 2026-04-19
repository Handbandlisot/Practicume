def numbers(x):
    '''
    Function displays the digits 
    of a natural number x in reverse order
    '''
    if x == 0:
        return 
    print(x % 10)
    numbers(x // 10)
    

numbers(123)
