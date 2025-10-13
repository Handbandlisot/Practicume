nu = int(input())
un = (nu % 10 * 1000) + ((nu - nu // 100 * 100) // 10) * 100 + (nu // 100 * 100 - nu // 1000 * 1000) // 10 +  nu // 1000
if nu == nu:
    print('Настоящее')
else:
    print('Кривое')
