num = int(input())

output = ""
if num == 1:
    output = "Monday"
elif num == 2:
    output = "Tuesday"
elif num == 3:
    output = "Wednesday"
elif num == 4:
    output = "Thursday"
elif num == 5:
    output = "Friday"
elif num == 6:
    output = "Saturday"
elif num == 7:
    output = "Sunday"
else:
    output = "Error"

print(output)