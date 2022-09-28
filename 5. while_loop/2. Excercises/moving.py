width = int(input())
length = int(input())
height = int(input())

total_space = width * length * height
is_full = False

command = input()
while command != "Done":
    current_boxes = int(command)
    total_space -= current_boxes
    if total_space <= 0:
        is_full = True
        break
    command = input()
if is_full:
    print(f"No more free space! You need {abs(total_space)} Cubic meters more.")
else:
    print(f"{total_space} Cubic meters left.")
