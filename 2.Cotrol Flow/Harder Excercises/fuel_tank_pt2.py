fuel_type = input()
fuel_liters = float(input())
club_card = input()

total = 0
if fuel_type == "Gas":
    price_per_liter = 0.93
    if club_card == "Yes":
        price_per_liter -= 0.08
    total = fuel_liters * price_per_liter
elif fuel_type == "Gasoline":
    price_per_liter = 2.22
    if club_card == "Yes":
        price_per_liter -= 0.18
    total = fuel_liters * price_per_liter
elif fuel_type == "Diesel":
    price_per_liter = 2.33
    if club_card == "Yes":
        price_per_liter -= 0.12
    total = fuel_liters * price_per_liter

if fuel_liters > 25:
    total *= 0.90
elif 20 <= fuel_liters <= 25:
    total *= 0.92

print(f"{total:.2f} lv.")