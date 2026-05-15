n = int(input())

dictionary = {}
for _ in range(n):
    parts = input().split()
    shape = parts[0]
    for item in parts[1:]:
        dictionary[item] = shape

word = input()

print(dictionary.get(word, word))