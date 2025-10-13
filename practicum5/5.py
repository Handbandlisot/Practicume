height = int(input())
weight = int(input())
bmi = round(weight / ((height / 100) ** 2), 2)
if bmi < 16:
    print('выраженный дефицит массы тела')
elif bmi < 18.49:
    print('недостаточная масса тела')
elif bmi < 24.99:
    print('норма')
elif bmi < 29.99:
    print('избыточная масса тела')
elif bmi < 34.99:
    print('ожирение первой степени')
elif bmi < 39.99:
    print('ожирение второй степени')
else:
    print('ожирение третей степени')
