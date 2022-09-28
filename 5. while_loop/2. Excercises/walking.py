command = input()
is_reached_goal = False

total_steps = 0
while command != "Going home":

    steps = int(command)
    total_steps += steps
    if total_steps >= 10000:
        is_reached_goal = True
        break
    command = input()

if command == "Going home":
    steps_to_home = int(input())
    total_steps += steps_to_home
    if total_steps >= 10000:
        is_reached_goal = True

diff = abs(total_steps - 10000)

if is_reached_goal:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")
