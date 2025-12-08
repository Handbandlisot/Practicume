nu = int(input('Введите число: '))
if nu**0.5 == int(nu**0.5):
    print('Полный квадрат')
else:
    print('Не полный квадрат')
    while nu**0.5 != int(nu**0.5):
        nu = int(input('Введите другое число: '))
        if nu**0.5 == int(nu**0.5):
            print('Полный квадрат')
