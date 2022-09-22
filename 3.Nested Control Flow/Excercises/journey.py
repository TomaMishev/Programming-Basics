budget = float(input())
season = input()

destination = ""
expanses = 0
place = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        expanses = budget * 0.30
        place = "Camp"
    elif season == "winter":
        expanses = budget * 0.70
        place = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        expanses = budget * 0.40
        place = "Camp"
    elif season == "winter":
        expanses = budget * 0.80
        place = "Hotel"
else:
    destination = "Europe"
    expanses = budget * 0.90
    place = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place} - {expanses:.2f}")
