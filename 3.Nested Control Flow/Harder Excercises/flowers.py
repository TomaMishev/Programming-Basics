chrysanthemum_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
is_holiday = input()

chrysanthemum_price = 0
roses_price = 0
tulips_price = 0

if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2
    roses_price = 4.10
    tulips_price = 2.50
elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15

bouquet_price = (chrysanthemum_count * chrysanthemum_price) + (roses_count * roses_price)\
                + (tulips_count * tulips_price)
if is_holiday == 'Y':
    bouquet_price *= 1.15

if season == "Spring" and tulips_count > 7:
    bouquet_price *= 0.95

if season == "Winter" and roses_count >= 10:
    bouquet_price *= 0.90

total_flowers = chrysanthemum_count + roses_count + tulips_count
if total_flowers > 20:
    bouquet_price *= 0.80

bouquet_price += 2

print(f"{bouquet_price:.2f}")