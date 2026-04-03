def discount(cost: int, card: bool, holiday: bool):
    '''
    Count the discount amount
    '''
    discount = 0
    
    if card:
        discount += 5
    if holiday:
        discount += 3
    
    if cost > 5000:
        return cost - ((discount + 3) / 100 * cost)
    elif cost > 15000:
        return cost - ((discount + 5) / 100 * cost)
    elif cost > 20000:
        return cost - ((discount + 7) / 100 * cost)
    elif cost > 30000:
        discount += 10

        if discount > 15:
            return cost * 0.85
        else:
            return cost - (discount / 100 * cost)
        
    else:
        return cost - (discount / 100 * cost)


print(round(discount(34343, True, True), 2))
