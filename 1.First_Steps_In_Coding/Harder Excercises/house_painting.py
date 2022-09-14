house_height = float(input())
side_length = float(input())
roof_height = float(input())

side_left = house_height * side_length
window_area = 1.5 * 1.5
both_sides_area = (2 * side_left) - (2 * window_area)

rear_side_area = house_height * house_height
entrance = 1.2 * 2
front_side_back_side_total = rear_side_area * 2 - entrance

total_area = both_sides_area + front_side_back_side_total

green_paint = total_area / 3.4

roof_sides = 2 * (house_height * side_length)
roof_fronts = 2 * (house_height * roof_height / 2)
total_area = roof_sides + roof_fronts

red_paint = total_area / 4.3

print(f"{green_paint:.2f}\n{red_paint:.2f}")
