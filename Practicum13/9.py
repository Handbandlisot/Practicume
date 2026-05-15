from itertools import combinations

numbers = sorted(set(map(int, input().split())))
k = int(input())

result = [list(subset) for subset in combinations(numbers, k)]

print(result)
