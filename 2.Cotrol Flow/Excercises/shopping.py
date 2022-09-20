budget = float(input())
video_cards_count = int(input())
processors_count = int(input())
ram_count = int(input())

video_cards_price = video_cards_count * 250
processors_price = video_cards_price * 0.35
processors_total_price = processors_price * processors_count
ram_price = video_cards_price * 0.10
ram_total_price = ram_price * ram_count

total_sum = video_cards_price + processors_total_price + ram_total_price

if video_cards_count > processors_count:
    total_sum = total_sum * 0.85

diff = abs(budget - total_sum)

if budget >= total_sum:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
