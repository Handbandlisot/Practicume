order = int(input())
for i in range(0, order // 5 + 2):
    if (order - i * 5) % 7 == 0:
        print('да')
        break
    if order - i * 5 < 0:
        print('нет')
        break
