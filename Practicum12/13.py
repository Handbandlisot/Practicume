def odd_list(a, n):
    '''
    Function returns a list of even values ​
    ​from a list containing n integer elements.
    '''
    if n == 0:
        return []
    if a[0] % 2 == 0:
        return [a[0]] + odd_list(a[1:], n - 1)
    else:
        return odd_list(a[1:], n - 1)    

print(odd_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))
