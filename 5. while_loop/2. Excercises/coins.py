change = float(input())
coins = round(change * 100)

total_coins = 0

while coins > 0:
    if coins >= 200:
        coins -= 200
        total_coins += 1
    elif coins >= 100:
        coins -= 100
        total_coins += 1
    elif coins >= 50:
        coins -= 50
        total_coins += 1
    elif coins >= 20:
        coins -= 20
        total_coins += 1
    elif coins >= 10:
        coins -= 10
        total_coins += 1
    elif coins >= 5:
        coins -= 5
        total_coins += 1
    elif coins >= 2:
        coins -= 2
        total_coins += 1
    elif coins >= 1:
        coins -= 1
        total_coins += 1

print(total_coins)
