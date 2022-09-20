trip_price = float(input())
puzzel_count = int(input())
doll_count = int(input())
teddy_count = int(input())
minion_count = int(input())
trucks_count = int(input())

puzzel_price = puzzel_count * 2.60
doll_price = doll_count * 3.00
teddy_price = teddy_count * 4.10
minion_price = minion_count * 8.20
trucks_price = trucks_count * 2.00

total_price = puzzel_price + doll_price + teddy_price + minion_price + trucks_price
total_toy_count = puzzel_count + doll_count + teddy_count + minion_count + trucks_count

if total_toy_count >= 50:
    total_price = total_price * 0.75

total_price = total_price * 0.90

diff = abs(trip_price - total_price)

if total_price >= trip_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
