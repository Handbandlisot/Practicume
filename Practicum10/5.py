def phone_card():
    cost = int(input())
    
    if cost == 5 or cost == 10:
        return cost
    elif cost == 25:
        return cost + 3
    elif cost == 50:
        return cost + 8
    elif cost == 100:
        return cost + 20
    else:
        print('Wrong card cost')


phone_card()
