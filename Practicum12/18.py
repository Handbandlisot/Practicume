def simmetr(s, i, j):
    '''
    Function determines whether the part of the string s, 
    starting with the i-th character and 
    ending with the j-th, is symmetrical
    '''
    if i >= j:
        return True
    if s[i] != s[j]:
        return False
    return simmetr(s, i + 1, j - 1)


print(simmetr('SALAv', 0, 4))
