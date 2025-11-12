import math as m

x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())

d = m.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
if d > r1 + r2:
    print('Окружности лежат одна вне другой, не касаясь')
elif d == r1 + r2:
    print('Окружности имеют внешнее касание')
elif d < r1 + r2 and d > abs(r1 - r2):
    print('Окружности пересекаются')
elif d == abs(r1 - r2):
    print('Окружности имеют внутреннее касание')
if d < abs(r1 - r2):
    print('Одна окружность лежит внутри другой, не касаясь')
