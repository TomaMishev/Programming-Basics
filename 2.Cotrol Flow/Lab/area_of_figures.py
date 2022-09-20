import math

figure = input()
result = 0

if figure == "square":
    side = float(input())
    result = side * side
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    result = side_a * side_b
elif figure == "circle":
    radius = float(input())
    result = math.pi * radius ** 2
elif figure == "triangle":
    side_a = float(input())
    side_h = float(input())
    result = side_a * side_h / 2

print(f"{result:.3f}")