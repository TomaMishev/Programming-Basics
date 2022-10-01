sold_games_count = int(input())

hearthstone_count = 0
fortnite_count = 0
overwatch_count = 0
others_count = 0

for game in range(1, sold_games_count + 1):
    current_game = input()
    if current_game == "Hearthstone":
        hearthstone_count += 1
    elif current_game == "Fornite":
        fortnite_count += 1
    elif current_game == "Overwatch":
        overwatch_count += 1
    else:
        others_count += 1

hearthstone_percentage = hearthstone_count / sold_games_count * 100
fortnite_percentage = fortnite_count / sold_games_count * 100
overwatch_percentage = overwatch_count / sold_games_count * 100
others_percentage = others_count / sold_games_count * 100

print(f"Hearthstone - {hearthstone_percentage:.2f}%")
print(f"Fornite - {fortnite_percentage:.2f}%")
print(f"Overwatch - {overwatch_percentage:.2f}%")
print(f"Others - {others_percentage:.2f}%")
