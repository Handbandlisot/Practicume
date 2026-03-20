def dividers(number):
    div = []

    for num in range(1, int(number ** 0.5) + 1):
        if number % num == 0:
            div.append(num)
            div.append(number // num)

    return sorted(div)

def common_multiples(a, b, n):
    a_div = dividers(a)
    b_div = dividers(b)
    
    for div in max(a_div, b_div, key=len):
        if div in a_div and b_div and div <= n:
            print(div, end=' ')


common_multiples(100, 1000, 50)
