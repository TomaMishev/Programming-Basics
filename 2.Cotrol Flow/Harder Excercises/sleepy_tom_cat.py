days_off = int(input())

working_days = 365 - days_off
total_play_time = (working_days * 63) + (days_off * 127)
norm_diff = abs(30000 - total_play_time)
hours = norm_diff // 60
minutes = norm_diff % 60

if 30000 >= total_play_time:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")