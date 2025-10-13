fir, sec, thi = map(int, input().split())
if fir >= sec and fir >= thi:
    if sec >= thi:
        print(fir, sec, thi)
    else:
        print(fir, thi, sec)
elif sec >= fir and sec >= thi:
    if fir >= thi:
        print(sec, fir, thi)
    else:
        print(sec, thi, fir)
else:
    if fir >= sec:
        print(thi, fir, sec)
    else:
        print(thi, sec, fir)
