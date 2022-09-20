budget = float(input())
statists_count = int(input())
clothes_per_statists_price = float(input())

decor = budget * 0.10
total_clothes_price = statists_count * clothes_per_statists_price

if statists_count > 150:
    total_clothes_price = total_clothes_price * 0.90

total_budget = decor + total_clothes_price
diff = abs(total_budget - budget)

if budget >= total_budget:
    print(f"Action!\nWingard starts filming with {diff:.2f} leva left.")
else:
    print(f"Not enough money!\nWingard needs {diff:.2f} leva more.")