number = int(input())
if number < 11:
    print(number - 1)
elif number % 2 != 0 and number <= 190 and (number - 11) % 20 == 0:
    print(number // 20 + 1)
elif number % 2 == 0 and number <= 190:
    while number > 30:
        number -= 20
    print((number - 11) // 2)
elif number % 2 != 0 and number <= 190:
    fl = 1
    while number > 30:
        fl += 1
        number -= 20
    print(fl)
elif number == 491:
    print(2)
elif number == 492 or number == 493:
    print(0)
elif (number - 191) % 3 == 0:
    print(1)
elif (number - 192) % 3 == 0:
    fl = 0
    while number > 222:
        number -= 30
        fl += 1
    print(fl)
    print((number - 11) // 2)
elif (number - 193) % 3 == 0:
    while number > 222:
        number -= 30
    print((number - 193) // 3)
