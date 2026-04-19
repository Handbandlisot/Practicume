def search(a, x):
    '''
    Function determines whether the integer values 
    ​​in a list a contain a number x
    '''
    if len(a) == 1 and a[0] != x:
        return 0
    if a[0] == x:
        return 1
    else:
        return search(a[1:], x)
    

print(search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))
