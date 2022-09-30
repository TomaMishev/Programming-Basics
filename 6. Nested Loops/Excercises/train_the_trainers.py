jury_count = int(input())

input_line = input()
presentation_count = 0
all_grades = 0
while input_line != "Finish":
    presentation_name = input_line
    total_grades = 0
    for grade in range(jury_count):
        current_grade = float(input())
        total_grades += current_grade
        all_grades += current_grade
        presentation_count += 1
    avg_grade = total_grades / jury_count

    print(f"{presentation_name} - {avg_grade:.2f}.")
    input_line = input()
final_avg = all_grades / presentation_count
print(f"Student's final assessment is {final_avg:.2f}.")