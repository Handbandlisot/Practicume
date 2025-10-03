first, second = map(int, input().split(':'))
if first > second:
    print('1')
elif second > first:
    print('2')
else:
    print('0')
