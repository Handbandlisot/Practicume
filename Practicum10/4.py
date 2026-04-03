def make_payment(P):
    '''
    Makes a payment and checks its success
    '''
    try:
        P = int(P)
        if P > 1000 or P < 20:
            print('Повторить попытку')
        else:
            print('Успех')
    except ValueError:
        print('Повторить попытку')


make_payment(35)
