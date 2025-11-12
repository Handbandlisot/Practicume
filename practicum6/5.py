place1, place2 = map(str, input().split('-'))
letter1, number1 = int(place1[0], 20) - 9, int(place1[1])
letter2, number2 = int(place2[0], 20) - 9, int(place2[1])
if number1 + 2 == number2 and (letter1 - 1 == letter2 or letter1 + 1 == letter2):
    print('верно')
elif number1 - 2 == number2 and (letter1 - 1 == letter2 or letter1 + 1 == letter2):
    print('верно')
elif letter1 - 2 == letter2 and (number1 - 1 == number2 or number1 + 1 == number2):
    print('верно')
elif letter1 + 2 == letter2 and (number1 - 1 == number2 or number1 + 1 == number2):
    print('верно')
else:
    print('неверно')
