def simple(number):
    for div in range(2, int(number ** 0.5) + 1):
        if number % div == 0:
            return False
    return True


n = int(input())
for number in range(1, n):
    if simple(number):
        print(number, end=' ')
