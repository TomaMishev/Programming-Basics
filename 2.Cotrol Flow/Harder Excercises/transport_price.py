distance = int(input())
text = input()

price = 0
if distance < 20:
    if text == 'day':
        price = 0.70 + (distance * 0.79)
    elif text == 'night':
        price = 0.70 + (distance * 0.90)
elif distance < 100:
    price = distance * 0.09
else:
    price = distance * 0.06

print(f"{price:.2f}")