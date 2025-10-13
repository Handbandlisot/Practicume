knat = int(input())
sikl = knat // 29
knat -= sikl * 29
galleon = sikl // 17
sikl -= galleon * 17
if galleon > 0:
    print(galleon, 'галлеонов')
if sikl > 0:
    print(sikl, 'сиклей')
if knat > 0:
    print(knat, 'кнатов')
