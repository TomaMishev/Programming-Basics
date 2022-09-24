season = input()
km_per_month = float(input())

pay_per_km = 0
if season == "Spring" or season == "Autumn":
    if km_per_month <= 5000:
        pay_per_km = 0.75
    elif 5000 < km_per_month <= 10000:
        pay_per_km = 0.95
elif season == "Summer":
    if km_per_month <= 5000:
        pay_per_km = 0.90
    elif 5000 < km_per_month <= 10000:
        pay_per_km = 1.10
elif season == "Winter":
    if km_per_month <= 5000:
        pay_per_km = 1.05
    elif 5000 < km_per_month <= 10000:
        pay_per_km = 1.25
if 10000 < km_per_month <= 20000:
    pay_per_km = 1.45

wage = km_per_month * pay_per_km
wage_after_tax = wage * 4 * 0.90
print(f"{wage_after_tax:.2f}")