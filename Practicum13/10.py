from itertools import combinations


nums = list(map(int, input().split()))

result = {tuple(sorted(triple)) for triple in combinations(nums, 3) if sum(triple) == 0}

print([list(t) for t in result])
