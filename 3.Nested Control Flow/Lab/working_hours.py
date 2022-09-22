time = int(input())
day = input()

status = "closed"
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" \
        or day == "Friday" or day == "Saturday":
    if 10 <= time <= 18:
        status = "open"
print(status)
