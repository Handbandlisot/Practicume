def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def months_leap(is_leap):
    if is_leap:
        months = [0, 31, 60, 91, 
                  121, 152, 182, 213, 
                  244, 274, 305, 335]
    else:
        months = [0, 31, 59, 90, 
                  120, 151, 181, 212, 
                  243, 273, 304, 334] 
    return months

def second_counter(time: str):
    time = time.split(' ')
    date = time[0].split('/')
    time_of_date = time[1].split(':')
    months = months_leap(is_leap(int(date[2])))

    days = int(date[1]) + months[int(date[0]) - 1]
    days_second = (days - 1) * 24 * 60 * 60
    time_second = int(time_of_date[0]) * 60 * 60
    time_second += int(time_of_date[1]) * 60 + int(time_of_date[2])
    
    return days_second + time_second


print(second_counter("03/20/2026 10:07:40"))
