actor_name = input()
starting_points = float(input())
total_actors = int(input())

copy_starting_points = starting_points
for i in range(1, total_actors + 1):
    current_actor = input()
    points = float(input())
    total_points = len(current_actor) * points / 2
    copy_starting_points += total_points
    if copy_starting_points > 1250.5:
        break
if copy_starting_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {copy_starting_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {abs(1250.5 - copy_starting_points):.1f} more!")