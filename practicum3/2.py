second = int(input())
hour = second / 60 // 60
second -= hour * 60 ** 2
minute = second // 60
second -= minute * 60
print(f'{int(hour)} часов {int(minute)} минут {int(second)} секунд')
