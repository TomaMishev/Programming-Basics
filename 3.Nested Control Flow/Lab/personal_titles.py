age = float(input())
gender = input()

output = ""
if gender == 'f':
    if age < 16:
        output = "Miss"
    else:
        output = "Ms."
elif gender == 'm':
    if age < 16:
        output = "Master"
    else:
        output = "Mr."
print(output)