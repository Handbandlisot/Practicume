n = int(input())

dictionary = {}
for _ in range(n):
    a, b = input().split()
    dictionary[a] = b
    dictionary[b] = a

word = input()

print(dictionary.get(word, word))