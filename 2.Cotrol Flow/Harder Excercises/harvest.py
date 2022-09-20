import math

vineyard_area = int(input())
grape_for_square_M = float(input())
liters_needed = int(input())
workers = int(input())

total_grape = vineyard_area * grape_for_square_M
wine = (0.40 * total_grape) / 2.5

if wine >= liters_needed:
    left_wine = wine - liters_needed
    wine_per_worker = left_wine / workers
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    print(f"{math.ceil(left_wine)} liters left -> {math.ceil(wine_per_worker)} liters per person.")
else:
    diff = liters_needed - wine
    print(f"It will be a tough winter! More {math.floor(diff)} liters wine needed.")
