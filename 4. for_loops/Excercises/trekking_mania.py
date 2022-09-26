climber_groups = int(input())

g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0

total_climbers = 0
for i in range(1, climber_groups + 1):
    current_group = int(input())
    if current_group <= 5:
        g1 += current_group
    elif 6 <= current_group <= 12:
        g2 += current_group
    elif 13 <= current_group <= 25:
        g3 += current_group
    elif 26 <= current_group <= 40:
        g4 += current_group
    else:
        g5 += current_group

    total_climbers += current_group

g1_percent = g1 / total_climbers * 100
g2_percent = g2 / total_climbers * 100
g3_percent = g3 / total_climbers * 100
g4_percent = g4 / total_climbers * 100
g5_percent = g5 / total_climbers * 100

print(f"{g1_percent:.2f}%")
print(f"{g2_percent:.2f}%")
print(f"{g3_percent:.2f}%")
print(f"{g4_percent:.2f}%")
print(f"{g5_percent:.2f}%")

