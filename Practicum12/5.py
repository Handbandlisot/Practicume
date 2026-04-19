def mod_number(a, b):
    '''
    Function finds the remainder when dividing 
    a natural number a by a natural number b
    '''
    if a < b:
        return a
    else:
        return mod_number(a - b, b)
    

print(mod_number(102, 3))
