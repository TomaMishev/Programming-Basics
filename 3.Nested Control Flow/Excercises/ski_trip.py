days_stay = int(input())
room_type = input()
grade = input()

nights_stay = days_stay - 1

total_price = 0
if room_type == "room for one person":
    total_price = 18 * nights_stay
elif room_type == "apartment":
    total_price = 25 * nights_stay
    if nights_stay < 10:
        total_price *= 0.70
    elif 10 <= nights_stay <= 15:
        total_price *= 0.65
    else:
        total_price *= 0.50
elif room_type == "president apartment":
    total_price = 35 * nights_stay
    if nights_stay < 10:
        total_price *= 0.90
    elif 10 <= nights_stay <= 15:
        total_price *= 0.85
    else:
        total_price *= 0.80

if grade == "positive":
    total_price *= 1.25
elif grade == "negative":
    total_price *= 0.90

print(f"{total_price:.2f}")

