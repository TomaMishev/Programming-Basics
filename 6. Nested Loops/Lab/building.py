floors = int(input())
rooms = int(input())
room_type_index = ''

for current_floor in range(floors, 0, -1):
    for current_room in range(rooms):
        if current_floor == floors:
            room_type_index = 'L'
        elif current_floor % 2 == 0:
            room_type_index = 'O'
        else:
            room_type_index = 'A'
        print(f"{room_type_index}{current_floor}{current_room}", end=" ")
    print()