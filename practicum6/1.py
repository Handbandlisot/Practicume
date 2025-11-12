lenght, width = map(int, input().split('x'))
if lenght ** 2 + width ** 2 <= 169:
    print('да')
else:
    print('нет')
