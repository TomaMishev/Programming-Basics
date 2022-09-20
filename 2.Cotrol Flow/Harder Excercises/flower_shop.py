import math

magnolias_count = int(input())
hyacinths_count = int(input())
roses_count = int(input())
cacti_count = int(input())
present_price = float(input())

magnolias_price = magnolias_count * 3.25
hyacinths_price = hyacinths_count * 4
roses_price = roses_count * 3.50
cacti_price = cacti_count * 8

total_price = magnolias_price + hyacinths_price + roses_price + cacti_price
total_price *= 0.95

diff = abs(total_price - present_price)

if total_price >= present_price:
    print(f"She is left with {math.floor(diff)} leva.")
else:
    print(f"She will have to borrow {math.ceil(diff)} leva.")