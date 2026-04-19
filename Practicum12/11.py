def ind_maxlist(a):
    '''
    Function calculats the index of the maximum element 
    of a list of integer elements
    '''
    if len(a) == 1:
        return 0
    if a[0] > a[1 + ind_maxlist(a[1:])]:
        return 0
    else:
        return 1 + ind_maxlist(a[1:])
    

print(ind_maxlist([2, 3, 4, 1, 5, 7, 8, 2, 5, 8, 10, 56, 12, 43, 23, 21]))

