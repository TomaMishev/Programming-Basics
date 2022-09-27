student_name = input()
current_class = 1
is_expelled = False
rejected_counter = 0
total_grades_score = 0
while current_class <= 12:
    current_grade = float(input())
    if current_grade < 4:
        rejected_counter += 1
        if rejected_counter == 2:
            is_expelled = True
            break
        continue

    current_class += 1
    total_grades_score += current_grade

if is_expelled:
    print(f"{student_name} has been excluded at {current_class} grade")
else:
    avg_grade = total_grades_score / 12
    print(f"{student_name} graduated. Average grade: {avg_grade:.2f}")
