kids, capacity, minutes = map(int, input().split())
if kids * 2 % capacity == 0:
    print(kids * 2 // capacity * minutes)
else:
    print((kids * 2 // capacity + 1) * minutes)
