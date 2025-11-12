place = str(input())
letter = int(place[0], 20) + 1
number = int(place[1])
if number % 2 == letter % 2:
    print('черный')
else:
    print('белый')
