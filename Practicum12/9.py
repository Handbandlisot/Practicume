def combin(n, k):
    '''
    Function calculates a combinatorial combination
    '''
    if k == 0:
        return 1
    if k == 1:
        return n
    if n == k:
        return 1
    if k > n:
        return 0
    return combin(n - 1, k - 1) + combin(n - 1, k)


print(combin(5, 4))
