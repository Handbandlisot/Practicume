x, y = map(int, input().split())
nu_del_x = x // y
nu_del_y = y // x
print((x == nu_del_x * y) + (y == nu_del_y * x))
