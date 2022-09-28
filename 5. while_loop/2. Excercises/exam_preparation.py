unsatisfactory_grades = int(input())
unsatisfactory_grades_count = 0
is_failed = False
total_grades = 0
total_problems = 0
last_problem = ""
while True:
    problem_name = input()
    if problem_name == "Enough":
        is_failed = False
        break
    grade = int(input())
    if grade <= 4:
        unsatisfactory_grades_count += 1
        if unsatisfactory_grades_count == unsatisfactory_grades:
            is_failed = True
            break
    total_grades += grade
    total_problems += 1
    last_problem = problem_name

if is_failed:
    print(f"You need a break, {unsatisfactory_grades} poor grades.")
else:
    avg_score = total_grades / total_problems
    print(f"Average score: {avg_score:.2f}")
    print(f"Number of problems: {total_problems}")
    print(f"Last problem: {last_problem}")
