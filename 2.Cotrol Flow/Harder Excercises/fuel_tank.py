text = input()
fuel_liters = float(input())

output = ''
if text == 'Diesel':
    if fuel_liters >= 25:
        output = f"You have enough {text.lower()}."
    else:
        output = f"Fill your tank with {text.lower()}!"
elif text == 'Gasoline':
    if fuel_liters >= 25:
        output = f"You have enough {text.lower()}."
    else:
        output = f"Fill your tank with {text.lower()}!"
elif text == 'Gas':
    if fuel_liters >= 25:
        output = f"You have enough {text.lower()}."
    else:
        output = f"Fill your tank with {text.lower()}!"
else:
    output = "Invalid fuel!"

print(output)

