import math as m

xvl1, yvl1 = map(int, input().split())
xnp1, ynp1 = map(int, input().split())
shi1 = xnp1 - xvl1
dli1 = yvl1 - ynp1
xvl2, yvl2 = map(int, input().split())
xnp2, ynp2 = map(int, input().split())
shi2 = xnp2 - xvl2
dli2 = yvl2 - ynp2

if xnp1 < xvl2 or ynp1 > yvl2 or xvl1 > xnp2 or yvl1 < ynp2:
    print('Прямоугольники лежат вне друг друга, не касаясь')
elif xnp1 == xvl2 and ynp1 <= yvl2 and dli1 + dli2 >= yvl2-ynp1:
    print('Прямоугольники имеют касание')
elif xnp2 == xvl1 and ynp2 <= yvl1 and dli1 + dli2 >= yvl1-ynp2:
    print('Прямоугольники имеют касание')
elif ynp1 == yvl2 and xnp1 >= xvl2 and shi1 + shi2 >= xnp1 - xvl2:
    print('Прямоугольники имеют касание')
elif ynp2 == yvl1 and xnp2 >= xvl1 and shi1 + shi2 >= xnp2 - xvl1:
    print('Прямоугольники имеют касание')
elif ynp1 > ynp2 and xnp1 < xnp2 and yvl1 < yvl2 and xvl1 > xvl2:
    print('Один прямоугольник лежит внутри другого, не касаясь')
elif ynp2 > ynp1 and xnp2 < xnp1 and yvl2 < yvl1 and xvl2 > xvl1:
    print('Один прямоугольник лежит внутри другого, не касаясь')
else:
    print('Прямоугольники имеют пересечение')
