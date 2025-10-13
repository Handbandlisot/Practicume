password = int(input())
cor = 0
if len(str(password)) == 4:
    f = password // 1000
    s = password // 100 - f * 10
    t = password // 10 - f * 100 - s * 10
    l = password % 10
    if f != s and f != t and f != l and s != t and s != l and t != l:
        if password < 1900 or password > 2050:
            print('OK')
        else:
            print('ERROR')
    else:
        print('ERROR')       
else:
    print('ERROR')
