import string


lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

full_text = " ".join(lines).lower()
translator = str.maketrans('', '', string.punctuation)
clean_text = full_text.translate(translator)

words = clean_text.split()

if words:
    sorted_words = sorted(words, key=lambda w: words.count(w), reverse=True)

    seen = set()
    result = []
    for w in sorted_words:
        if w not in seen:
            result.append(w)
            seen.add(w)

    print(*result, sep='\n')
