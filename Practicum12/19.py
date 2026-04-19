def count(a, b):
    '''
    Function calculates how many squares can be cut off
    '''
    if a == b:
        return 1
    if a > b:
        return 1 + count(a - b, b)
    else:
        return 1 + count(a, b - a)
    

print(count(10, 3))