hours_init = int(input())
min_init = int(input())

total_time = (hours_init * 60) + min_init + 15

hours = total_time // 60
min = total_time % 60

if hours >= 24:
    hours = 0

if min <= 9:
    print(f"{hours}:0{min}")
else:
    print(f"{hours}:{min}")