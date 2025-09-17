from math import *
a = int(input())
b = int(input())
c = int(input())
print(degrees(acos((c**2 + b**2 - a**2) / (2 * b * c))))
print(degrees(acos((c**2 + a**2 - b**2) / (2 * a * c))))
print(degrees(acos((a**2 + b**2 - c**2) / (2 * a * b))))
