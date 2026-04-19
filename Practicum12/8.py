def fbk(k):
    '''
    Function calculates the k-th term of the Fibonacci sequence
    '''
    if k <= 2:
        return 1
    else:
        return fbk(k - 1) + fbk(k - 2)
    

print(fbk(7))
