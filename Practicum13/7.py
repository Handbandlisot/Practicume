from itertools import permutations


numbers = sorted(set(map(int, input().split())))

for p in permutations(numbers):
    print(*p)
