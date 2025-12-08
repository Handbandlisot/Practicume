n = int(input())
f = 0
out = ''
while (f+1)**3 <= n:
    f += 1
    out += str(f**3) + ' '
print(out)
