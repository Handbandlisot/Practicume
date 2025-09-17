n = float(input())
hours = int(n // 30)
minutes = int((n - hours * 30) // 0.5)
print(hours, minutes)
