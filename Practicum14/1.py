words = input().lower().replace(',', '').replace('.', '').replace('!', '').split()

counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1

for word, count in sorted(counts.items(), key=lambda x: -x[1]):
    print(word)