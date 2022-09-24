budget = float(input())
category = input()
fans_count = int(input())

expanses_for_transport = 0
if 1 <= fans_count <= 4:
    expanses_for_transport = budget * 0.75
elif 5 <= fans_count <= 9:
    expanses_for_transport = budget * 0.60
elif 10 <= fans_count <= 24:
    expanses_for_transport = budget * 0.50
elif 25 <= fans_count <= 49:
    expanses_for_transport = budget * 0.40
else:
    expanses_for_transport = budget * 0.25

ticket_price = 0
if category == "VIP":
    ticket_price = 499.99 * fans_count
elif category == "Normal":
    ticket_price = 249.99 * fans_count

budget = budget - expanses_for_transport

diff = abs(budget - ticket_price)

if budget >= ticket_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
