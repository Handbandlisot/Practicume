x, y = map(int, input().split('x'))
k = int(input())
if (k % x == 0 or k % y == 0) and x * y >= k:
    print('успешно')
else:
    print('неосуществимо')
