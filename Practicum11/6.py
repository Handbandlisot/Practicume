num = int(input())

list_of_dividers = []

for div in range(2, int(num ** 0.5) + 1):
    if num % div == 0:
        list_of_dividers.append(div)
        list_of_dividers.append(num // div)
        
print(list_of_dividers)
