text = 'haha   text      about  spaces        '

c = 0
k = 0
for i in range(len(text)):
    if text[i] == ' ':
        c += 1
        k = max(k, c)
    else:
        c = 0
print(k)
