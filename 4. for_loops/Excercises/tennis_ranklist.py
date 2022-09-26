import math

tournament_count = int(input())
starting_points = int(input())

win_games = 0
total_points = 0
for i in range(1, tournament_count + 1):
    index = input()
    if index == "W":
        total_points += 2000
        win_games += 1
    elif index == "F":
        total_points += 1200
    elif index == "SF":
        total_points += 720

all_points = starting_points + total_points
avg_points = math.floor(total_points / tournament_count)
win_percent = win_games / tournament_count * 100

print(f"Final points: {all_points}\nAverage points: {avg_points}\n{win_percent:.2f}%")