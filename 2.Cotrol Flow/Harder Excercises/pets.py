import math

missing_days = int(input())
left_food = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_gr = float(input())

dog_needed_food = missing_days * dog_food_kg
cat_needed_food = missing_days * cat_food_kg
turtle_needed_food = missing_days * turtle_food_gr / 1000
total_food = dog_needed_food + cat_needed_food + turtle_needed_food

diff = abs(left_food - total_food)

if left_food >= total_food:
    print(f"{math.floor(diff)} kilos of food left.")
else:
    print(f"{math.ceil(diff)} more kilos of food are needed.")