n = int(input())

dictionary = {}
for _ in range(n):
    ru, en = input().split()
    dictionary[ru] = en

phrase = input().lower().split()

print(*[dictionary.get(w, w) for w in phrase])