n = int(input())
f = 0
while n != 1:
    f += 1
    if n % 2 == 0:
        n //= 2
    else:
        n = n // 2 + 1
print(f)
