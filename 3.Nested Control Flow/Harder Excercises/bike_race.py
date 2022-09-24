juniors_count = int(input())
seniors_count = int(input())
trek_type = input()

all_racers = juniors_count + seniors_count

total_price = 0
if trek_type == "trail":
    total_price = (juniors_count * 5.50) + (seniors_count * 7)
elif trek_type == "cross-country":
    total_price = (juniors_count * 8) + (seniors_count * 9.50)
    if all_racers >= 50:
        total_price *= 0.75
elif trek_type == "downhill":
    total_price = (juniors_count * 12.25) + (seniors_count * 13.75)
elif trek_type == "road":
    total_price = (juniors_count * 20) + (seniors_count * 21.50)

total_price *= 0.95

print(f"{total_price:.2f}")


