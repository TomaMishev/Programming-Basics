trunk_capacity = float(input())
command_line = input()
briefcase_count = 0
is_full = False
loaded_suitcase = 0
while command_line != "End":
    current_briefcase_volume = float(command_line)
    briefcase_count += 1
    if briefcase_count % 3 == 0:
        current_briefcase_volume *= 1.10
    if current_briefcase_volume > trunk_capacity:
        is_full = True
        break
    trunk_capacity -= current_briefcase_volume
    loaded_suitcase += 1

    command_line = input()
if is_full:
    print(f"No more space!")
    print(f"Statistic: {loaded_suitcase} suitcases loaded.")
else:
    print(f"Congratulations! All suitcases are loaded!")
    print(f"Statistic: {loaded_suitcase} suitcases loaded.")
