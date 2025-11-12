x, y = map(int, input().split('x'))
x1, y1, z1 = map(int, input().split('x'))
if x1 * y1 <= x * y:
    print('да')
elif x1 * z1 <= x * y:
    print('да')
elif z1 * y1 <= x * y:
    print('да')
else:
    print('нет')
