x = int(input())
if x % 2 == 0:
    while x % 2 == 0 and x != 1:
        x //= 2
    if x == 1:
        print('верно')
    else:
        print('неверно')
else:
    print('неверно')
