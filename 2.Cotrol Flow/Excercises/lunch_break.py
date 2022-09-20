import math

show_name = input()
episode_length = int(input())
break_length = int(input())

lunch_length = break_length / 8
chill_length = break_length / 4
time_left = break_length - lunch_length - chill_length

if time_left >= episode_length:
    print(f"You have enough time to watch {show_name} and left with {math.ceil(time_left - episode_length)} minutes "
          f"free time.")
else:
    print(f"You don't have enough time to watch {show_name}, you need {math.ceil(episode_length - time_left)} more "
          f"minutes.")
