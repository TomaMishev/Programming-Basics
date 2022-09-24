season = input()
group = input()
students_count = int(input())
nights_count = int(input())

price_for_night = 0
if season == "Winter":
    price_for_night = 9.60
    if group == "mixed":
        price_for_night = 10
elif season == "Spring":
    price_for_night = 7.20
    if group == "mixed":
        price_for_night = 9.50
elif season == "Summer":
    price_for_night = 15
    if group == "mixed":
        price_for_night = 20

sport_type = ""
if season == "Winter":
    if group == "girls":
        sport_type = "Gymnastics"
    elif group == "boys":
        sport_type = "Judo"
    elif group == "mixed":
        sport_type = "Ski"
elif season == "Spring":
    if group == "girls":
        sport_type = "Athletics"
    elif group == "boys":
        sport_type = "Tennis"
    elif group == "mixed":
        sport_type = "Cycling"
elif season == "Summer":
    if group == "girls":
        sport_type = "Volleyball"
    elif group == "boys":
        sport_type = "Football"
    elif group == "mixed":
        sport_type = "Swimming"

total_price = students_count * nights_count * price_for_night

if 10 <= students_count < 20:
    total_price *= 0.95
elif 20 <= students_count < 50:
    total_price *= 0.85
elif students_count >= 50:
    total_price *= 0.50

print(f"{sport_type} {total_price:.2f} lv.")

