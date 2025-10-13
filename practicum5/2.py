from turtle import *
from math import sqrt

tracer(0)
left(90)
xc = int(input())
yc = int(input())
r = int(input())
x = int(input())
y = int(input())
d = sqrt((x - xc) ** 2 + (y - yc) ** 2)
if d < r:
    print('Точка внутри окружности')
elif d == r:
    print('Точка на окружности')
else:
    print('Точка вне окружности')
up()
forward(yc)
right(90)
forward(xc)
down()
circle(r)
up()
forward(-xc)
left(90)
forward(-yc)
forward(y)
forward(r)
right(90)
forward(x)
down()
dot(3, 'red')

done()
