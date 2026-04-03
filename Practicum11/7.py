list = [int(num) for num in input().split()]

print(sum([num for num in list if num % 2 == 0]))
print(sum([num for num in list if num % 2 != 0]))
