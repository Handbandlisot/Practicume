def maxlist(a):
    '''
    Function calculats the maximum element 
    of a list of integer elements
    '''
    if len(a) == 1:
        return a[0]
    if a[0] > maxlist(a[1:]):
        return a[0]
    else:
        return maxlist(a[1:])
    

print(maxlist([1, 5, 7, 8, 2, 5, 8, 10, 56, 12, 43, 23, 21]))
