first_set = set(map(int, input().split()))
second_set = set(map(int, input().split()))
number = int(input())

if number in first_set & second_set:
    print('Yes')
else:
    print('No')
