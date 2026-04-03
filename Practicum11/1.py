list = []
another_list = []

for _ in range(10):
    list.append(int(input()))
    
for num in range(1, 9):
    another_list.append(list[num - 1] + list[num])

print(another_list)
