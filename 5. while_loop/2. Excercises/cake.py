width = int(input())
height = int(input())

total_pieces = width * height
is_left = True

command = input()
while command != "STOP":
    current_pieces = int(command)
    total_pieces -= current_pieces
    
    if total_pieces <= 0:
        is_left = False
        break

    command = input()

if not is_left:
    print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
else:
    print(f"{total_pieces} pieces are left.")
