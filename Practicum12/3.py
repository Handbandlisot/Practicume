def progress(a1, r, n):
    '''
    Function finds the n-th term of a progression
    '''
    if n == 1:
        return a1
    else:
        return r + progress(a1, r, n - 1)
    

print(progress(3, 7, 3))
