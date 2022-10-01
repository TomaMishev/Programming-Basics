days_count = int(input())

total_money = 0
total_wins = 0
total_losses = 0
for day in range(days_count):
    sport = input()
    win_per_day = 0
    lose_per_day = 0
    money_for_day = 0
    while sport != "Finish":
        outcome = input()
        if outcome == "win":
            win_per_day += 1
            total_wins += 1
            money_for_day += 20
        elif outcome == "lose":
            lose_per_day += 1
            total_losses += 1
        sport = input()
    if win_per_day > lose_per_day:
        money_for_day *= 1.10
    total_money += money_for_day
if total_wins > total_losses:
    total_money *= 1.20
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")