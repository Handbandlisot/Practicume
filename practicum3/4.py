x, y, n = map(int, input().split())
x, y = x*n, y*n
x += y // 100
y -= y // 100 * 100
print(f'{x} рублей {y} копеек')
