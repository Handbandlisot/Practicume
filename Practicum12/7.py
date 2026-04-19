def nod(a, b):
    '''
    Function calculates the greatest common divisor 
    of two natural numbers a and b
    '''
    if b == 0:
        return a
    else:
        return nod(b, a % b)
    

print(nod(15, 5))
