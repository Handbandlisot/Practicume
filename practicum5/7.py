su, current, want = map(int, input().split())
go = max(want - current, current - want)
notgo = su - current + want
if go > notgo:
    print(notgo - 1)
else:
    print(go - 1)
