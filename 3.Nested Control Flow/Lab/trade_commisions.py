town = input()
sales_qty = float(input())

commission = 0
if town == "Sofia":
    if 0 <= sales_qty <= 500:
        commission = 0.05
    elif 500 < sales_qty <= 1000:
        commission = 0.07
    elif 1000 < sales_qty <= 10000:
        commission = 0.08
    else:
        commission = 0.12
elif town == "Varna":
    if 0 <= sales_qty <= 500:
        commission = 0.045
    elif 500 < sales_qty <= 1000:
        commission = 0.075
    elif 1000 < sales_qty <= 10000:
        commission = 0.10
    else:
        commission = 0.13
elif town == "Plovdiv":
    if 0 <= sales_qty <= 500:
        commission = 0.055
    elif 500 < sales_qty <= 1000:
        commission = 0.08
    elif 1000 < sales_qty <= 10000:
        commission = 0.12
    else:
        commission = 0.145
if commission == 0 or sales_qty < 0:
    print("error")
else:
    total = sales_qty * commission
    print(f"{total:.2f}")