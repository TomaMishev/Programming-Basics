input_line = input()

total_tickets = 0
standard_tickets = 0
student_tickets = 0
kids_tickets = 0

while input_line != "Finish":

    movie_name = input_line
    free_seats = int(input())
    command_name = input()



    current_tickets = 0
    while command_name != "End":
        if command_name == "student":
            current_tickets += 1
            student_tickets += 1
            total_tickets += 1
        elif command_name == "standard":
            current_tickets += 1
            standard_tickets += 1
            total_tickets += 1
        elif command_name == "kid":
            current_tickets += 1
            kids_tickets += 1
            total_tickets += 1
        if current_tickets == free_seats:
            break
        command_name = input()

    percentage = current_tickets / free_seats * 100
    print(f"{movie_name} - {percentage:.2f}% full.")

    input_line = input()

print(f"Total tickets: {total_tickets}")
student_percentage = student_tickets / total_tickets * 100
standard_percentage = standard_tickets / total_tickets * 100
kids_percentage = kids_tickets / total_tickets * 100
print(f"{student_percentage:.2f}% student tickets.")
print(f"{standard_percentage:.2f}% standard tickets.")
print(f"{kids_percentage:.2f}% kids tickets.")