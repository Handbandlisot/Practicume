first = int(input())
second = int(input())
third = int(input())
smile = (first == second) + (first == third) + (second == third)
if smile == 1:
    print(smile + 1)
else:
    print(smile)
