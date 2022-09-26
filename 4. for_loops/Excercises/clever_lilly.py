age = int(input())
washing_machine_price = float(input())
toy_price = float(input())

money = 10
saved_money = 0
toy_count = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        saved_money += (money - 1)
        money += 10
    else:
        toy_count += 1

toy_money = toy_price * toy_count
total_money = saved_money + toy_money

diff = abs(total_money - washing_machine_price)

if total_money >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")

