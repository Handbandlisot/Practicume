x = ''
count = 0
for i in range(100, 1000):
    if i % 17 == 0:
        count += 1
        x += str(i) + ' '
print(x)
print(count)
