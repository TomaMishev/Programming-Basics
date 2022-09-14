import math

radius = float(input())
area = math.pi * math.pow(radius, 2)
perimeter = 2 * math.pi * radius

print(f"{area:.2f}\n{perimeter:.2f}")