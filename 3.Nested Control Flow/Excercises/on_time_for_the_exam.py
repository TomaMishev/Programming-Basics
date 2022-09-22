exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

total_exam_minutes = (exam_hour * 60) + exam_minutes
total_arrival_minutes = (arrival_hour * 60) + arrival_minutes

diff = abs(total_exam_minutes - total_arrival_minutes)

status = ""
output = "20 minutes after the start"
if total_arrival_minutes > total_exam_minutes:
    status = "Late"
    if diff < 60:
        minutes = diff % 60
        output = f"{minutes} minutes after the start"
    else:
        hours = diff // 60
        minutes = diff % 60
        if minutes <= 9:
            output = f"{hours}:0{minutes} hours after the start"
        else:
            output = f"{hours}:{minutes} hours after the start"

elif total_arrival_minutes == total_exam_minutes or diff <= 30:
    status = "On time"
    minutes = diff % 60
    output = f"{minutes} minutes before the start"
else:
    status = "Early"
    if diff < 60:
        minutes = diff % 60
        output = f"{minutes} minutes before the start"
    else:
        hours = diff // 60
        minutes = diff % 60
        if minutes <= 9:
            output = f"{hours}:0{minutes} hours before the start"
        else:
            output = f"{hours}:{minutes} hours before the start"

print(status)
print(output)
