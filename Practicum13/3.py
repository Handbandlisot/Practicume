sweet_tooth = set(input().split())
sweet_friends = int(input())

for _ in range(sweet_friends):
    sweet_tooth -= set(input().split())

print(len(sweet_tooth))
