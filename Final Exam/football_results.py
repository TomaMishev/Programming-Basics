first_game_result = input()
second_game_result = input()
third_game_result = input()

won_games = 0
lost_games = 0
draw_games = 0

first_game_home_score = int(first_game_result[0])
first_game_away_score = int(first_game_result[2])
if first_game_home_score > first_game_away_score:
    won_games += 1
elif first_game_home_score < first_game_away_score:
    lost_games += 1
else:
    draw_games += 1

second_game_home_result = int(second_game_result[0])
second_game_away_result = int(second_game_result[2])
if second_game_home_result > second_game_away_result:
    won_games += 1
elif second_game_away_result > second_game_home_result:
    lost_games += 1
else:
    draw_games += 1

third_game_home_result = int(third_game_result[0])
third_game_away_result = int(third_game_result[2])
if third_game_home_result > third_game_away_result:
    won_games += 1
elif third_game_home_result < third_game_away_result:
    lost_games += 1
else:
    draw_games += 1

print(f"Team won {won_games} games.")
print(f"Team lost {lost_games} games.")
print(f"Drawn games: {draw_games}")