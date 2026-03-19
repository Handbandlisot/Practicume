def fib(number):
    first_num = 1
    second_num = 1
    print(first_num, second_num, end=' ')
    for _ in range(number - 2):
        between_num = first_num + second_num
        print(between_num, end=' ')
        first_num = second_num
        second_num = between_num


fib(10)
