def ten_to_bin(x):
    '''
    Function converts natural numbers x from decimal to binary
    '''
    if x == 0:
        return ''
    return ten_to_bin(x // 2) + str(x % 2)


print(ten_to_bin(1))
