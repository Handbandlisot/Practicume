def check_of_numbers(num_a, num_b):
    if num_a > num_b:
        num_a, num_b = num_b, num_a
    statement = set({1, 3, 4, 8, 9})
    for number in range(num_a, num_b + 1):
        if len(list(condition for condition in statement if str(condition) in str(number))) == len(statement):
            print(number, end=' ')


check_of_numbers(10000, 14000)
