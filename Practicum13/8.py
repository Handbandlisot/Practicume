from itertools import combinations

numbers = sorted(set(map(int, input().split())))
powerset = []

for r in range(len(numbers) + 1):
    for subset in combinations(numbers, r):
        powerset.append(list(subset))

print(powerset)
