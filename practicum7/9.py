n, k, r = map(int, input().split())
k = 1 + k / 100
day = 1
while n < r:
    day += 1
    n *= k
print(day)
