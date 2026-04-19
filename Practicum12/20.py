from functools import lru_cache


@lru_cache(None)
def comp(a, b, m, n):
    '''
    Function finds the length of the common subsequence 
    of characters of strings a and b
    '''
    if m == 0 or n == 0:
        return 0
    if a[m-1] == b[n-1]:
        return 1 + comp(a, b, m-1, n-1)
    else:
        return max(comp(a, b, m, n-1), comp(a, b, m-1, n))
    

print(comp('BAB', 'BAA', 3, 3))
