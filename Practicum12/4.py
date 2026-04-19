def sum_progress(a1, r, n):
    '''
    Function finds the sum of n terms of a progression.
    '''
    if n == 1:
        return a1
    else:
        return a1 + r * (n - 1) + sum_progress(a1, r, n - 1)
    

print(sum_progress(2, 2, 1))
