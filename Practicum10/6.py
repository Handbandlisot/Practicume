def sms_check(text):
    '''
    Limits SMS size to 160
    '''
    return text[:160]


print(sms_check('yriutrtiuiu'))
