length = float(input())
width = float(input())

length_cm = length * 100
width_cm = width * 100
width_cm -= 100

desk_per_row = width_cm // 70
rows = length_cm // 120

total_space = desk_per_row * rows - 3

print(f"{total_space:.0f}")
