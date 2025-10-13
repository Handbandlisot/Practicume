pop = int(input())
if pop % 10 == 1 and pop != 11:
    print(pop, 'попугай')
elif pop % 10 > 1 and pop % 10 < 5 and (pop < 12 or pop > 14):
    print(pop, 'попугая')
else:
    print(pop, 'попугаев')
