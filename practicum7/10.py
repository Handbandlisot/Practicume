x = str(input())
x1 = x
f = 0
while x != '0' and x1 != '0':
    x1 = str(input())
    if float(x1) - float(x) < 0:
        f += 1
    x = x1
print(f)
